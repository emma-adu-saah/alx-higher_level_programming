#!/usr/bin/python3
"""Lists all cities from the database hbtn_0e_4_usa"""
import sys
import MySQLdb

ARGS = sys.argv[1:]


def list_all_cities(username, password, db_name):
    """List all cities from the database hbtn_0e_4_usa"""
    db = MySQLdb.connect(host="localhost",
                         user=username,
                         passwd=password,
                         db=db_name)
    cursor = db.cursor()
    cursor.execute("SELECT cities.id,\
                    cities.name,\
                    states.name\
                    FROM cities LEFT JOIN states\
                    ON states.id = cities.state_id\
                    ORDER BY cities.id")
    result = cursor.fetchall()
    for row in result:
        print(row)


if __name__ == "__main__":
    username = ARGS[0]
    password = ARGS[1]
    db_name = ARGS[2]

    list_all_cities(username, password, db_name)
