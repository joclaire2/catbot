
import sqlite3

def exec_sql(sql):
    conn = sqlite3.connect('../sqllite/catbot.db')
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()
    
# exec_sql("DROP TABLE cat_owners")

# exec_sql("CREATE TABLE cat_owners (date text, owner text)")

#exec_sql("INSERT INTO cat_owners (date, owner) VALUES ('2019-10-08 19:10:10','Ribman')")

#result = query_sql("SELECT * FROM cat_owners")
#for row in result:
#    print(f"result: {row}")