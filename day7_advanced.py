from langchain_groq import ChatGroq
from langchain.tools import tool
from langchain.agents import create_agent
import logging
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Setup Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("Calculator_Agent")

@tool
def add(a: float, b: float) -> float:
    """Adds two numbers."""
    logger.info(f"add executed: {a} + {b}")
    return a + b

@tool
def multiply(a: float, b: float) -> float:
    """Multiplies two numbers."""
    logger.info(f"multiply executed: {a} * {b}")
    return a * b

@tool
def divide(a: float, b: float) -> str:
    """Divides two numbers."""
    if b == 0:
        return "Cannot divide by zero."
    return str(a / b)

# Initialize the LLM (Brain)
llm = ChatGroq(model="llama-3.3-70b-versatile", api_key=os.getenv("GROQ_API_KEY"))

# Define the Job Description
system_prompt = """You are an expert calculator.
ALWAYS use tools for mathematical operations.
Provide clear and concise answers in English."""

# Create the Agent (Factory)
agent = create_agent(llm, [add, multiply, divide], system_prompt=system_prompt)

# Helper Function
def process_query(question):
    try:
        logger.info(f"Question: {question}")
        result = agent.invoke({"messages": [("user", question)]})
        return result["messages"][-1].content
    except Exception as e:
        logger.error(f"Error: {e}")
        return "System is busy, please try again later."

# ===== EXECUTION =====
question = "First add 10 and 5, then multiply by 3"
answer = process_query(question)

print("\nFINAL ANSWER:")
print(answer)