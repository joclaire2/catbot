
import sqlite3

dbPath = '../sqllite/catbot.db'

def exec_sql(sql):
    conn = sqlite3.connect(dbPath)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()

def query_sql(sql):
    conn = sqlite3.connect(dbPath)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute(sql)
    result = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return result
               
result = query_sql("SELECT * FROM cat_owners")
for row in result:
    print(f"result: {row}")
	