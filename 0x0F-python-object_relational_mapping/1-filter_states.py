#!/usr/bin/python3
"""Lists all states with a name starting with N"""
import MySQLdb
import sys

ARGS = sys.argv[1:]


def list_states_with_n(username, password, db_name):
    """Lists all states that starts with N"""
    db = MySQLdb.connect(host="localhost",
                         user=username,
                         passwd=password,
                         db=db_name)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE BINARY name LIKE 'N%' ORDER BY id")
    result = cursor.fetchall()

    for row in result:
        print(row)

    db.close()


if __name__ == "__main__":
    username = ARGS[0]
    password = ARGS[1]
    db_name = ARGS[2]

    list_states_with_n(username, password, db_name)
