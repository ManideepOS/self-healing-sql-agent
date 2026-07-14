from src.database import run_query

print("--- Test 1: Testing a perfect query ---")
good_result = run_query("SELECT * FROM lending_portfolio WHERE risk_segment = 'High Risk'")
print(good_result)

print("\n--- Test 2: Testing a broken query (Typo in table name) ---")
bad_result = run_query("SELECT * FROM broken_table_name")
print(bad_result)