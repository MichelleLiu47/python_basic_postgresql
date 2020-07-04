import psycopg2

# connect to the db
con = psycopg2.connect(
    host="localhost",
    database="my_db",
    user="postgres",
    password="123456")

# cursor
cur = con.cursor()

# cur.execute("insert into employees (id,name) values(6,'Ali');")

cur.execute("insert into employees (id,name) values(%s,%s)", (8, "pop"))

# execute query
cur.execute("select id, name from employees")

rows = cur.fetchall()

for r in rows:
    print(f"id {r[0]} name {r[1]}")

# commit the transactions
con.commit()

# close the cursor
cur.close()

# close the connection
con.close()
