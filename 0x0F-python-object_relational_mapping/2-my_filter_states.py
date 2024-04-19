#!/usr/bin/python3
"""
Script that displays all values in the states table of hbtn_0e_0_usa
where name matches the provided argument
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2],
                           db=argv[3],
                           charset="utf8")

    cursor = conn.cursor()

    query = "SELECT * FROM states WHERE\
        name = '{}' ORDER BY states.id ASC".format(argv[4])

    cursor.execute(query)

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    conn.close()
