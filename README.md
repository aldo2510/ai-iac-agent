# AI IaC Agent

Local AI agent for generating governed Terraform through Ollama and the IaC MCP Server.

## Flow

```
Developer -> Ollama -> MCP -> approved Terraform module -> Git branch -> PR
```

The agent is intentionally designed so that infrastructure changes are reviewed in GitHub instead of being applied directly by the model.

## Prerequisites

- Python 3.11+
- Ollama
- A local model such as `qwen2.5:7b` or another tool-capable model
- `iac-mcp-server` available locally

## Run

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export OLLAMA_MODEL=qwen2.5:7b
python agent.py
```
