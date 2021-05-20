import sqlite3
import time

conn = sqlite3.connect('main.db')

c = conn.cursor()

date = time.time

c.execute("INSERT INTO MAIN VALUES('')")

c.execute("SELECT * FROM MAIN WHERE first=date")

print(c.fetchall())

conn.commit()
conn.close