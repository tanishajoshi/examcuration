""" Sqlite specific reader. """

import sqlite3

class SqliteReader():
    """ Module for handling reading from Sqlite. """

    def __init__(self, db_name):
        """ Construct handle based on db name. """

        self.db_name = db_name

    def query(self, sql):
        """ Generic query execution and return list. """

        with sqlite3.connect(self.db_name) as conn:
            cur = conn.cursor()
            try:
                cur.execute(sql)
            except sqlite3.OperationalError as oper_error:
                raise ValueError(oper_error)
            return cur.fetchall()

    def execute(self, table, **kwargs):
        """ Dynamic predicate construction and execution. """

        sub_predicates = []
        for args in kwargs:
            sub_predicates.append(f"{args}='{kwargs[args]}'")

        if len(sub_predicates) > 0:
            predicate = ' AND '.join(sub_predicates)
            query = f'SELECT * FROM {table} WHERE {predicate}'
        else:
            query = f'SELECT * FROM {table}'

        return self.query(query)
