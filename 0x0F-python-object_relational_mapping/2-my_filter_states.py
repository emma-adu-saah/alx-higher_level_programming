#!/usr/bin/python3
"""Takes an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument
"""
import sys
import MySQLdb

ARGS = sys.argv[1:]


def list_states_by_input(username, password, db_name, name):
    """Displays all values in the states by user input"""
    db = MySQLdb.connect(host="localhost",
                         user=username,
                         passwd=password,
                         db=db_name)
    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name = {} ORDER BY id".format(name)
    print(query)
    cursor.execute(query)
    result = cursor.fetchall()

    for row in result:
        print(row)


if __name__ == "__main__":
    username = ARGS[0]
    password = ARGS[1]
    db_name = ARGS[2]
    name = ARGS[3]

    list_states_by_input(username, password, db_name, name)
