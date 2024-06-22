#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa"""
import sys
import MySQLdb


def list_database(username, passwd, db_name):
    """A function Lists all states from hbtn_0e_0_usa"""

    # Connect to the database.
    db = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=passwd,
        db=db_name
        )

    # Create a cursor that will execute SQL queries
    cur = db.cursor()
    # Use cursor to execute queries
    cur.execute("SELECT * FROM states")

    # Fetch result using cursor object
    results = cur.fetchall()
    cur.close()
    db.close()
    return (results)


if __name__ == "__main__":
    # Create variables to store the commandline arguements
    ARGS = sys.argv[1:]
    username = ARGS[0]
    passwd = ARGS[1]
    db_name = ARGS[2]

    rows = list_database(username, passwd, db_name)
    for row in rows:
        print(row)
