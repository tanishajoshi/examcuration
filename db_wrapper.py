# disabling:
# C0301: Line too long (line-too-long)
# pylint: disable=C0301
'''Module for database'''
import sqlite3
from csvreader import read_file, write_file

connection = sqlite3.connect("qadb.db")
cursor = connection.cursor()
cursor.execute("CREATE TABLE question (qID INTEGER, question TEXT, qTypeID INTEGER, createDate, updateDate)")


def main():
    '''Main function'''
    write_file()
    read_file()

if __name__ == "__main__":
    main()
