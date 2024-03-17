#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
import sys

ARGS = sys.argv[1:]


def lists_states(username, password, db_name):
    """Connects to a database and lists states"""
    db = MySQLdb.connect(host="localhost",
                         user=username,
                         passwd=password,
                         db=db_name)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id")
    result = cursor.fetchall()
    for row in result:
        print(row)
    db.close()


if __name__ == "__main__":
    username = ARGS[0]
    password = ARGS[1]
    db_name = ARGS[2]

    lists_states(username, password, db_name)
