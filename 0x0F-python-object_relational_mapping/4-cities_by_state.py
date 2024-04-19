#!/usr/bin/python3
"""script that lists all cities from
the database hbtn_0e_4_usa"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2],
                           db=argv[3],
                           charset="utf8")

    cursor = conn.cursor()

    query = "SELECT * FROM cities ORDER BY cities.id ASC"
    cursor.execute(query)

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    conn.close()
