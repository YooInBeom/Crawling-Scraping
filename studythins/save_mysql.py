import MySQLdb
from save_sqlite import conn

db = MySQLdb.connect(db='scraping', user='scraper', passwpd='password', charset='utf8mb4')

c = conn.cursor()

c.execute('DROP TABLE IF EXISTS cities')
c.execute('''
    CREATE TABLE cities (
        'rank' integer,
        city text,
        population integer
            )
        ''')

c.execute('INSERT INTO cities VALUES (%s, %s, %s,)', (1, '상하이', 24150000))
c.execute('INSERT INTO cities VALUES (:rank, :city, :population)',
          {'rank': 2, 'city': '카리치', 'population': 23500000})
c.executemany('INSERT INTO cities VALUES (:rank, :city, :population)', [
    {'rank': 3, 'city': '베이징', 'population': 21516000},
    {'rank': 4, 'city': '텐진', 'population': 1472200},
    {'rank': 5, 'city': '이스탄불', 'population': 14160467},
])

db.commit()

c.execute('SELECT * FROM cities')
for row in c.fetchall():
    print(row)

db.close()