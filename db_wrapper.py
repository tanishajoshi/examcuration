import csv
from csvreader import read_file, write_file

import sqlite3
"""
connection = sqlite3.connect("qadb.db")
cursor = connection.cursor()
cursor.execute("CREATE TABLE question (qID INTEGER, question TEXT, qTypeID INTEGER, createDate, updateDate)")

"""

def main():
    write_file()
    read_file()
    

if __name__ == "__main__":
    main()