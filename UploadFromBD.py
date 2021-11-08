import sqlite3
con = sqlite3.connect('classes_db.sqlite')
cur = con.cursor()
all_heroes = {}
all_abilities = {}
result = cur.execute("""SELECT * FROM Heroes""").fetchall()
result2 = cur.execute("""SELECT * FROM abilities""").fetchall()
for el in result:
    im = el[0]
    all_heroes[im] = []
    for i in range(1, len(el)):
        all_heroes[im].append(el[i])
for elm in result2:
    name = elm[0]
    all_abilities[name] = []
    for j in range(1, len(elm)):
        all_abilities[name].append(elm[j])
print(all_heroes)
print(all_abilities)