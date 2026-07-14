import duckdb

# 1. Create and connect to a brand new database file inside our data folder
conn = duckdb.connect('data/portfolio.db')
cursor = conn.cursor()

# 2. Build a fake table for consumer lending accounts
cursor.execute("""
    CREATE TABLE IF NOT EXISTS lending_portfolio (
        account_id VARCHAR,
        risk_segment VARCHAR,
        balance DOUBLE,
        delinquency_days INTEGER
    )
""")

# 3. Insert a few practice rows (representing standard, high-risk, and late accounts)
cursor.execute("""
    INSERT INTO lending_portfolio VALUES 
    ('ACC-001', 'Low Risk', 4500.50, 0),
    ('ACC-002', 'Medium Risk', 12000.00, 15),
    ('ACC-003', 'High Risk', 850.25, 45),
    ('ACC-004', 'Low Risk', 3100.00, 0)
""")

# 4. Save and close
conn.commit()
conn.close()

print("Success! Your safe financial database playground ('data/portfolio.db') has been created.")