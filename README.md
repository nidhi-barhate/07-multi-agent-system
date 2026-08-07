# 🤖 Multi-Agent System

> A production-inspired Multi-Agent AI framework built using Python that demonstrates intelligent planning, agent orchestration, parallel execution, tool calling, and reusable AI components.

---

# 📌 Overview

Modern AI applications are no longer powered by a single LLM prompt.

Instead, they consist of multiple specialized AI agents working together to solve complex problems.

This project demonstrates how to build an enterprise-inspired **Multi-Agent System** capable of:

- Planning tasks
- Delegating work to specialized agents
- Executing research in parallel
- Using external tools automatically
- Leveraging an Advanced RAG engine as a reusable Python package
- Producing high-quality reviewed responses

The architecture follows concepts used by modern AI frameworks such as:

- LangGraph
- CrewAI
- AutoGen
- Microsoft Semantic Kernel

---

# 🚀 Features

## 🤖 Multi-Agent Architecture

The system consists of multiple specialized AI agents.

- Orchestrator Agent
- Planner Agent
- Research Agent
- Reviewer Agent

Each agent has a single responsibility, making the system modular and extensible.

---

## 🧠 Intelligent Planning

Before solving a task, the Planner Agent automatically creates an execution plan.

Example:

**Input**

```
Design an AWS Serverless Image Upload Application
```

Planner Output

```
1. Analyze requirements
2. Select AWS services
3. Design architecture
4. Storage strategy
5. Security considerations
6. Deployment approach
```

---

## ⚡ Parallel Research

Instead of researching each step sequentially, multiple Research Agents execute simultaneously using:

- ThreadPoolExecutor

Result:

- Faster execution
- Better scalability
- Enterprise workflow pattern

---

## 🔍 Advanced Knowledge Retrieval

The Research Agent does not directly ask the LLM.

Instead, it retrieves trusted knowledge using the reusable **Advanced RAG Package**.

Capabilities include:

- Hybrid Search
- Semantic Search
- Keyword Search
- Re-ranking
- PDF Knowledge Base

---

## 🛠 Intelligent Tool Selection

Before creating an execution plan, the system determines whether a task should be handled by a tool.

Supported tools:

- Calculator
- Weather
- Current Time

Example

```
245 * 891
```

↓

Calculator Tool

instead of

Planner → Research → Reviewer

---

## 📝 Response Review

After all research completes, the Reviewer Agent:

- Merges results
- Removes duplicate information
- Improves readability
- Produces the final answer

---

# 🏗 Architecture

```text
                           User
                             │
                             ▼
                    Orchestrator Agent
                             │
                 Tool Selection (LLM)
                             │
          ┌──────────────────┴──────────────────┐
          ▼                                     ▼
 Calculator / Time / Weather              Planner Agent
                                                │
                                                ▼
                                         Execution Plan
                                                │
                ┌───────────────────────────────┼──────────────────────────────┐
                ▼                               ▼                              ▼
        Research Agent                  Research Agent                 Research Agent
          (Parallel)                      (Parallel)                     (Parallel)
                │                               │                              │
                └───────────────┬───────────────┴───────────────┬──────────────┘
                                ▼
                     Advanced RAG Package
                                │
         ┌──────────────────────┼──────────────────────┐
         ▼                      ▼                      ▼
   Hybrid Search         Semantic Search        Keyword Search
                                │
                                ▼
                           Re-ranking
                                │
                                ▼
                         Prompt Builder
                                │
                                ▼
                         Reviewer Agent
                                │
                                ▼
                          Final Response
```

---

# 📂 Project Structure

```text
multi-agent-system/

├── agents/
│      agent.py
│      assistant_agent.py
│      orchestrator_agent.py
│      planner_agent.py
│      research_agent.py
│      reviewer_agent.py
│
├── controllers/
│
├── models/
│      agent_result.py
│      execution_plan.py
│      tool_decision.py
│
├── prompts/
│      planner.txt
│      reviewer.txt
│      tool_selector.txt
│
├── services/
│      llm_service.py
│      tool_selection_service.py
│
├── tools/
│      calculator_tool.py
│      weather_tool.py
│      time_tool.py
│
├── shared-library/
│      └── advanced-rag/
│             ├── pyproject.toml
│             └── advanced_rag_bundle/
│
├── app.py
├── requirements.txt
└── README.md
```

---

# 📦 Shared Library

One of the objectives of this project is to demonstrate **modular AI application design**.

Instead of embedding Advanced RAG directly into the Multi-Agent System, it is packaged as a reusable Python library.

```
Multi-Agent System
        │
        ▼
Advanced RAG Package
        │
        ▼
Hybrid Search
Semantic Search
Keyword Search
Re-ranking
Prompt Builder
```

The reusable package is located under:

```
shared-library/
└── advanced-rag/
```

During development it can be installed using:

```bash
python -m pip install -e shared-library/advanced-rag
```

This demonstrates:

- Python Package Development
- Reusable AI Components
- Separation of Concerns
- Enterprise Software Architecture

---

# ⚙ Tech Stack

| Category | Technology |
|-----------|------------|
| Language | Python 3.11 |
| API | FastAPI |
| LLM | Ollama |
| Model | Qwen 3 |
| AI Pattern | Multi-Agent System |
| Parallel Execution | ThreadPoolExecutor |
| Knowledge Engine | Advanced RAG Package |
| Search | Hybrid Search |
| Package Management | pyproject.toml |

---

# 🔄 Workflow

```
User Request
      │
      ▼
Tool Selection
      │
      ▼
Planner Agent
      │
      ▼
Execution Plan
      │
      ▼
Parallel Research
      │
      ▼
Advanced RAG
      │
      ▼
Merge Results
      │
      ▼
Reviewer Agent
      │
      ▼
Final Response
```

---

# 🧪 Example Request

```json
{
    "task": "Design an AWS Serverless Image Upload Application"
}
```

---

# 📈 Example Execution

```
Planner

↓

Analyze Requirements

↓

Research AWS Services

↓

Research Storage

↓

Research Security

↓

Research Deployment

↓

Reviewer

↓

Final Architecture
```

---

# 🎯 Learning Outcomes

After completing this project you will understand:

- Multi-Agent Architecture
- Agent Orchestration
- Planner Agent Pattern
- Research Agent Pattern
- Reviewer Agent Pattern
- Tool Calling
- LLM Decision Making
- Parallel AI Execution
- ThreadPoolExecutor
- Advanced RAG Integration
- Python Package Development
- Reusable AI Components
- Enterprise AI Design Patterns
- Modular Software Architecture

---

# ⭐ Key Concepts Demonstrated

- Multi-Agent Systems
- Autonomous Planning
- Parallel Agent Execution
- Agent Collaboration
- Tool Selection
- Retrieval-Augmented Research
- Modular AI Architecture
- Reusable Python Packages
- Enterprise-inspired AI Design
