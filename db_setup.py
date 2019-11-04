
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

# cat_owners 

exec_sql("DROP TABLE IF EXISTS cat_owners")

exec_sql("CREATE TABLE cat_owners (id integer, owner_id text, join_date text, coins integer, last_daily text)")

exec_sql("DELETE FROM cat_owners WHERE owner_id='ribman'")

exec_sql("INSERT INTO cat_owners (id, owner_id, join_date, coins, last_daily) VALUES (1, 'ribman', '2019-10-08 19:10:10', 1, '2019-10-10 19:10:10')")

result = query_sql("SELECT * FROM cat_owners")
for row in result:
    print(f"result: {row}")


# cat_breeds 

exec_sql("DROP TABLE IF EXISTS cat_breeds")

exec_sql("CREATE TABLE cat_breeds (breed text)")

exec_sql("INSERT INTO cat_breeds (breed) VALUES ('Abyssinian'),('Burmese'),('Siamese'),('Tabby'),('Tortoiseshell')")

result = query_sql("SELECT * FROM cat_breeds")
for row in result:
    print(f"result: {row}")


# cats 

exec_sql("DROP TABLE IF EXISTS cats")

exec_sql("CREATE TABLE cats (id integer, name text, breed text, age integer, image text)")

exec_sql("INSERT INTO cats (id, name, breed, age, image) VALUES (1,'Timmy','Burmese',2,'https://www.purina.com/sites/g/files/auxxlc196/files/styles/kraken_generic_max_width_480/public/Burmese_body_6.jpg'), (2,'Jimmy','Siamese',5,'https://www.purina.com/sites/g/files/auxxlc196/files/styles/kraken_generic_max_width_480/public/Siamese_body_7.jpg') ")

result = query_sql("SELECT * FROM cats")
for row in result:
    print(f"result: {row}")


# cat_ownership 

exec_sql("DROP TABLE IF EXISTS cat_ownership")

exec_sql("CREATE TABLE cat_ownership (owner integer, cat integer)")

exec_sql("INSERT INTO cat_ownership (owner, cat) VALUES (1,1),(1,2)  ")

result = query_sql("SELECT * FROM cat_ownership")
for row in result:
    print(f"result: {row}")
	