import psycopg2
import os

conn = psycopg2.connect(
    host=os.getenv("DB_HOST", "postgres"),
    database=os.getenv("DB_NAME", "devops"),
    user=os.getenv("DB_USER", "devops"),
    password=os.getenv("DB_PASS", "devops")
)

def save_incident(log, result):
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS incidents (
            id SERIAL PRIMARY KEY,
            log TEXT,
            result TEXT
        )
    """)
    cur.execute("INSERT INTO incidents (log, result) VALUES (%s, %s)", (log, result))
    conn.commit()