import sqlite3
con = sqlite3.connect('classes_db.sqlite')
cur = con.cursor()
all_heroes = {}
result = cur.execute("""SELECT * FROM Heroes""").fetchall()
for el in result:
    im = el[0]
    all_heroes[im] = []
    for i in range(1, len(el)):
        all_heroes[im].append(el[i])
print(all_heroes)