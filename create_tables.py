import configparser
import psycopg2
from sql_queries import create_table_queries, drop_table_queries

"""
    drop_tables:
    function to execute all the drop tables queries from sql_queries.py
    args:
        cur: the database cursor object
        conn: the database connection object
"""


def drop_tables(cur, conn):
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


"""
    create_tables:
    function to execute all the creation table queries from sql_queries.py
    args:
        cur: the database cursor object
        conn: the database connection object
"""


def create_tables(cur, conn):
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


"""
    main:
    this is the main function, it will:
        - Create a connection object (conn)
        - Create a cursor object (cur)
        - Execute drop_tables
        - Execute create_tables
        - Close the connection to the database
"""


def main():
    config = configparser.ConfigParser()
    config.read("dwh.cfg")

    conn = psycopg2.connect(
        "host={} dbname={} user={} password={} port={}".format(
            *config["CLUSTER"].values()
        )
    )
    cur = conn.cursor()

    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()
