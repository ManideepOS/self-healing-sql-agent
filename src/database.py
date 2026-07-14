import duckdb

def run_query(sql_query: str):
    """
    The Robotic Glove: Takes a SQL string, tries to run it against 
    our fake database, and safely returns the data or the exact error.
    """
    try:
        # 1. Open the vault door
        conn = duckdb.connect('data/portfolio.db')
        cursor = conn.cursor()
        
        # 2. Try to run the query the AI gave us
        cursor.execute(sql_query)
        results = cursor.fetchall()
        
        # 3. Close the vault door safely
        conn.close()
        
        # Return a success message and the actual rows of data
        return {"status": "success", "data": results}
        
    except Exception as e:
        # 4. IF IT FAILS: Catch the exact error text instead of crashing!
        return {"status": "error", "message": str(e)}
    