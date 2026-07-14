from src.state import AgentState

# Simulate initializing an empty clipboard for a new user request
initial_clipboard: AgentState = {
    "user_question": "Show me total balance for High Risk accounts",
    "generated_sql": "",
    "error_message": "",
    "query_results": [],
    "retry_count": 0,
    "final_answer": ""
}

print("--- Clipboard Setup Successful ---")
print(f"Tracking Question: {initial_clipboard['user_question']}")
print(f"Current Retry Count: {initial_clipboard['retry_count']}")