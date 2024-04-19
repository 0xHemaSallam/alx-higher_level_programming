#!/usr/bin/python3
"""
Script that displays all values in the states table of hbtn_0e_0_usa
where name matches the provided argument
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Extract command-line arguments
    username = argv[1]
    password = argv[2]
    database = argv[3]
    state_name = argv[4]

    # Connect to the MySQL server
    conn = MySQLdb.connect(host="localhost", port=3306, user=username,
                           passwd=password, db=database, charset="utf8")

    # Create a cursor
    cursor = conn.cursor()

    # Prepare the SQL query using format
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY states.id ASC".format(state_name)

    # Execute the query
    cursor.execute(query)

    # Fetch all rows
    rows = cursor.fetchall()

    # Print the results
    for row in rows:
        print(row)

    # Close cursor and connection
    cursor.close()
    conn.close()
