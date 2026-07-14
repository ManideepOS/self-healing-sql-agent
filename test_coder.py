import os
from src.state import AgentState
from src.coder import generate_initial_sql

# Setup an initial mock clipboard
mock_state: AgentState = {
    "user_question": "Show me total balance for High Risk accounts",
    "generated_sql": "",
    "error_message": "",
    "query_results": [],
    "retry_count": 0,
    "final_answer": ""
}

print("--- Testing Coder Node ---")
# Invoke the node function directly
updates = generate_initial_sql(mock_state)

print("\n--- Test Results ---")
print(f"Updates payload returned: {updates}")