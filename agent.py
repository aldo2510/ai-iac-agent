import os
import json
import ollama

SYSTEM = """You are an Infrastructure as Code assistant.
Use only approved Terraform modules exposed by the MCP server.
Never invent module inputs.
Ask for missing required parameters.
Never execute terraform apply.
The final output must be suitable for a GitHub Pull Request review.
"""

def ask(prompt: str) -> str:
    response = ollama.chat(
        model=os.getenv("OLLAMA_MODEL", "qwen2.5:7b"),
        messages=[
            {"role": "system", "content": SYSTEM},
            {"role": "user", "content": prompt},
        ],
    )
    return response["message"]["content"]

if __name__ == "__main__":
    print("AI IaC Agent - type 'exit' to quit")
    while True:
        prompt = input("\n> ").strip()
        if prompt.lower() == "exit":
            break
        print("\n" + ask(prompt))
