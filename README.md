# 🤖 Autonomous LangChain Math Agent

A simple but powerful autonomous AI Agent built using Python, LangChain, and the Groq API (Llama 3). This agent acts as a smart calculator that strictly uses custom Python tools for mathematical accuracy instead of relying on the LLM's internal calculations.

## 🌟 Features
* **Custom Tools:** Uses LangChain `@tool` decorators for Addition, Multiplication, and Division.
* **High Performance:** Powered by Groq's lightning-fast `llama-3.3-70b-versatile` model.
* **Error Handling:** Built-in `try/except` blocks for safe execution without crashes.
* **System Logging:** Keeps a detailed backend log of user queries and tool executions.

## 🛠️ Prerequisites
Make sure you have Python installed, then install the required libraries:
```bash
pip install langchain langchain-groq python-dotenv
