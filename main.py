
import sqlite3
con = sqlite3.connect(input())
cur = con.cursor()
result1 = cur.execute("""SELECT films.title FROM films
            WHERE genre = ? and duration >= ?""", (1, 60)).fetchall()
for el in result1:
    print(el[0])
con.close()