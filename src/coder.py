import os
import re
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from src.state import AgentState

# 1. Define the structural database blueprint for the LLM
DB_SCHEMA = """
Table: portfolio
Columns:
  - account_id (VARCHAR): Unique identifier for the account
  - client_name (VARCHAR): Name of the institutional or retail client
  - balance (DOUBLE): Current total cash/asset valuation in USD
  - risk_profile (VARCHAR): Risk classification ('High Risk', 'Medium Risk', 'Low Risk')
  - asset_class (VARCHAR): Dominant asset type ('Equities', 'Fixed Income', 'Crypto', 'Cash')
"""

def generate_initial_sql(state: AgentState) -> dict:
    """
    The Coder Station: Takes the user's natural language question,
    looks at the schema blueprint, and generates a pure SQL query.
    """
    print(f"\n[Coder] Looking at question: '{state['user_question']}'")
    
    # Verify API key is configured before making the network call
    if not os.environ.get("OPENAI_API_KEY"):
        raise ValueError("CRITICAL: OPENAI_API_KEY environment variable is missing!")

    # Initialize our reasoning engine (using GPT-4o-mini for fast, accurate generation)
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

    # Construct the instruction guardrail prompt
    prompt = ChatPromptTemplate.from_messages([
        ("system", (
            "You are an elite quantitative data analyst specializing in DuckDB SQL.\n"
            "Your task is to translate a user's natural language question into a single valid DuckDB SQL query.\n\n"
            "CRITICAL RULES:\n"
            "1. Output ONLY the raw SQL code. No markdown formatting, no backticks, no markdown blocks, no commentary.\n"
            "2. Never start the response with words like 'Here is your query'.\n"
            "3. Use correct table and column names exactly as provided in the schema below.\n\n"
            "DATABASE SCHEMA:\n{schema}"
        )),
        ("human", "Translate this question to SQL: {question}")
    ])

    # Chain the prompt to the LLM and execute
    chain = prompt | llm
    response = chain.invoke({
        "schema": DB_SCHEMA,
        "question": state["user_question"]
    })

    raw_sql = response.content.strip()

    # Post-processing Guardrail: Clean out any accidental markdown triple-backticks if the LLM slipped up
    clean_sql = re.sub(r"```[a-zA-Z]*\n?", "", raw_sql).replace("```", "").strip()
    
    print(f"[Coder] Drafted SQL Query:\n{clean_sql}")
    
    # Return the modification to be merged into the clipboard
    return {"generated_sql": clean_sql}