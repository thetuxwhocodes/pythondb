#!/usr/bin/env python
# coding: utf-8

import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
 
    return conn



def select_all_users(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM Users")
 
    rows = cur.fetchall()
 
    for row in rows:
        print(row)


def main():
    database = "DMADb.db"
 
    # create a database connection
    conn = create_connection(database)
    with conn:
        print("1. Users:")
        select_all_users(conn)
 
 
if __name__ == '__main__':
    main()





