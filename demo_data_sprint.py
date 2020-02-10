#!/usr/bin/env python


import sqlite3

CONN = sqlite3.connect('demo_data.sqlite3')
DATA = [
    ('g', 3, 9),
    ('v', 5, 7),
    ('f', 8, 7)
]


def database():

    curs = CONN.cursor()
    curs.execute('CREATE TABLE demo (s char(1), x int, y int);')
    for i in DATA:
        curs.execute('INSERT INTO demo (s, x, y) VALUES ' + str(i))
    curs.close()
    CONN.commit()


def query():

    curs = CONN.cursor()
    print(curs.execute('SELECT COUNT(*) FROM demo;').fetchall())
    print(curs.execute('SELECT COUNT(*) FROM demo WHERE x >= 5 AND y >=5;').fetchall())
    print(curs.execute('SELECT COUNT(DISTINCT y) FROM demo;').fetchall())


if __name__ == "__main__":
    database()
    query()
