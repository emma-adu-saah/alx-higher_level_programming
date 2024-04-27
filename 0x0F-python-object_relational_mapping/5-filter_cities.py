#!/usr/bin/python3
"""Lists all cities from the database hbtn_0e_4_usa"""
import sys
import MySQLdb

ARGS = sys.argv[1:]


def list_all_cities(username, password, db_name, state):
    """List all cities from the database hbtn_0e_4_usa"""
    db = MySQLdb.connect(host="localhost",
                         user=username,
                         passwd=password,
                         db=db_name)
    cursor = db.cursor()
    cursor.execute(
        """SELECT cities.name FROM cities WHERE cities.state_id = (SELECT states.id FROM states WHERE states.name = %s) ORDER BY cities.id""", (state,))
    result = cursor.fetchall()
    print(f"This is result {result}")
    print(", ".join([row for row in result]))

    db.close()


if __name__ == "__main__":
    username = ARGS[0]
    password = ARGS[1]
    db_name = ARGS[2]
    state = ARGS[3]

    list_all_cities(username, password, db_name, state)
