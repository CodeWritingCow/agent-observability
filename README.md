# Agent Observability

An AI agent built with **LangChain**, **Ollama**, **Qwen**, and **Python**, with **LangSmith** tracing and monitoring for observing agent execution and LLM interactions.

This project is based on the freeCodeCamp tutorial:

> [How to Trace and Monitor AI Agents with LangSmith](https://www.freecodecamp.org/news/how-to-trace-and-monitor-ai-agents-with-langsmith/)

## Features

* 🤖 AI agent built with LangChain
* 🧠 Local LLM inference with Ollama and Qwen
* 🔍 LangSmith tracing
* 📊 Agent monitoring and observability
* 🔐 Environment variable management with `python-dotenv`

## Tech Stack

* **Python**
* **LangChain**
* **Ollama**
* **Qwen**
* **LangSmith**
* **python-dotenv**

## Prerequisites

Before running the project, install:

* Python 3.12+
* [Conda](https://docs.conda.io/)
* [Ollama](https://ollama.com/)
* A Qwen model available through Ollama
* A [LangSmith](https://smith.langchain.com/) account and API key

Verify that Ollama is installed:

```bash
ollama --version
```

Pull the Qwen model used by the project:

```bash
ollama pull qwen3.5:4b
```

You can use a different Qwen model by changing the model configuration in the project.

## Getting Started

### 1. Clone the repository

Using HTTPS:

```bash
git clone https://github.com/CodeWritingCow/agent-observability.git
cd agent-observability
```

Or using SSH:

```bash
git clone git@github.com:CodeWritingCow/agent-observability.git
cd agent-observability
```

### 2. Create a virtual environment

The project can be run using **Conda**, Python's built-in `venv`, or **uv**.

#### Conda

Create a new Conda environment:

```bash
conda create -n agent-observability python=3.12
```

Activate the environment:

```bash
conda activate agent-observability
```

#### Python `venv`

**Windows:**

```powershell
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

Install the dependencies from `requirements.txt`:

```bash
pip install -r requirements.txt
```

The project dependencies are:

```text
langchain
langchain-core
langchain-ollama
langsmith
python-dotenv
```

### 4. Configure environment variables

Create a `.env` file in the root directory:

```env
LANGSMITH_TRACING=true
LANGSMITH_ENDPOINT=https://api.smith.langchain.com
LANGSMITH_API_KEY=your-langsmith-api-key
LANGSMITH_PROJECT=your-project-name
```

`python-dotenv` loads these variables from the `.env` file when the application starts.

Replace `your-langsmith-api-key` with your LangSmith API key.

**Do not commit your `.env` file or LangSmith API key to Git.**

The `.env` file should be included in `.gitignore`.

### 5. Run the agent

Make sure Ollama is running and the Qwen model is available:

```bash
ollama list
```

Then run the agent:

```bash
python agent.py
```

After the agent runs, its traces can be viewed in the configured LangSmith project.

## Using uv

The project can also be installed and run using [uv](https://docs.astral.sh/uv/).

Create a virtual environment:

```bash
uv venv
```

Activate it:

**Windows:**

```powershell
.venv\Scripts\activate
```

**macOS/Linux:**

```bash
source .venv/bin/activate
```

Install the dependencies:

```bash
uv pip install -r requirements.txt
```

Run the agent:

```bash
uv run agent.py
```

## LangSmith Tracing

LangSmith provides observability into the agent's execution.

With tracing enabled, you can inspect information such as:

* Agent runs
* LLM calls
* Inputs and outputs
* Execution traces
* Latency
* Token usage
* Errors and failures

The application sends trace information to the LangSmith project specified by `LANGSMITH_PROJECT`.

After running the agent, open the project in LangSmith to inspect the recorded traces.

## Project Structure

```text
agent-observability/
├── agent.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

> **Note:** `.env` is shown for illustration only and should not be committed to the repository.

## Example Workflow

```text
User
  │
  ▼
LangChain Agent
  │
  ▼
Qwen via Ollama
  │
  ▼
Agent Response
  │
  └──────────────► LangSmith
                    │
                    ├── Traces
                    ├── LLM Calls
                    ├── Latency
                    ├── Token Usage
                    └── Errors
```

LangSmith runs alongside the application and records information about the agent's execution, making it possible to inspect individual runs and understand how the application behaved.

## Why Agent Observability?

As AI agents become more complex, understanding how an agent arrived at a result becomes increasingly important.

Tracing provides visibility into the individual steps of an agent's execution. This can help with debugging, identifying performance issues, analyzing model behavior, and monitoring applications over time.

## Tutorial

This project is based on the freeCodeCamp tutorial:

**[How to Trace and Monitor AI Agents with LangSmith](https://www.freecodecamp.org/news/how-to-trace-and-monitor-ai-agents-with-langsmith/)**

The project adapts the tutorial's concepts to a local AI environment using **Ollama** and **Qwen**.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
