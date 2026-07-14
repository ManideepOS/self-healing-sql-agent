from typing import TypedDict, List, Dict, Any

class AgentState(TypedDict):
    """
    The Shared Clipboard: This structure dictates exactly what our
    AI agent is allowed to look at and remember during its workflow.
    """
    # 1. The original question asked by the user
    user_question: str
    
    # 2. The current version of the SQL query the AI drafted
    generated_sql: str
    
    # 3. Any error message returned by our database glove (from Step 3)
    error_message: str
    
    # 4. The raw rows of data returned if the database query succeeds
    query_results: List[Any]
    
    # 5. Safety tracker: How many times have we tried to fix our own code?
    retry_count: int
    
    # 6. The final plain-English answer generated for the user
    final_answer: str