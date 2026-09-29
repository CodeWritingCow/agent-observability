from datetime import datetime

from langchain.agents import create_agent
from langchain_core.tools import tool
from langchain_ollama import ChatOllama

from dotenv import load_dotenv

load_dotenv()

CHAT_MODEL = "qwen3.5:4b"

SYSTEM_PROMPT = (
    "You are a helpful assistant with access to tools for getting the current time and counting words in text. "
    "Use tools when the user's request needs one. "
    "If the question doesn't need a tool, answer directly. "
    "If a tool returns an error, explain the error plainly."
)

# ----- Tools -----
@tool
def get_current_time() -> str:
    """Return the current local date and time.
    Use this when the user asks what time or date it is.
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

@tool
def count_words(text: str) -> int:
    """Count the number of words in a piece of text.
    Use this when the user asks how long a piece of writing is,
    or asks you to count the words in something they've shared.
    Returns the word count as an integer.
    """
    return len(text.split())

TOOLS = [get_current_time, count_words]

# ----- Agent -----
def build_agent():
    model = ChatOllama(model=CHAT_MODEL, reasoning=False, temperature=0)

    return create_agent(
        model=model,
        tools=TOOLS,
        system_prompt=SYSTEM_PROMPT
    )

def main():
    agent = build_agent()

    print("Ready! Ask the agent something.\n")

    # Track how many messages existed before this turn, so we can slice out
    # only the new ones (tool calls + final answer) from the returned state
    prev_message_count = 0

    while True:
        question = input("You: ").strip()
        if not question or question.lower() in ["exit", "quit"]:
            break

        result  = agent.invoke(
            {"messages": [{"role": "user", "content": question}]}
        )

        # Only look at messages added during this turn, not the full history
        new_messages = result["messages"][prev_message_count:]

        for message in new_messages:
            tool_calls = getattr(message, "tool_calls", None)
            if tool_calls:
                for call in tool_calls:
                    print(f"[tool call] {call['name']}({call['args']})")

        print(f"\nAnswer: {result['messages'][-1].content}\n")

        # Update count for next turn
        prev_message_count = len(result["messages"])


if __name__ == "__main__":
    main()