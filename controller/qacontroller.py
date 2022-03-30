# disabling:
# E0401: Unable to import
# pylint: disable=E0401
"""Controller module"""
from sqlite3 import Error
import sqlite3
from model.question import QConstants

def create_table(conn, create_table_sql):
    '''Create table in QADB'''
    try:
        conn_cursor = conn.cursor()
        conn_cursor.execute(create_table_sql)
    except Error as error:
        print(error)

def create_connection(db_file):
    '''Create connection to Sqlite'''
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as error:
        print(error)
    return conn

def call_create_table(db_file):
    '''Makes call to create table '''
    create_question_table = """ CREATE TABLE IF NOT EXISTS question (
        questionId integer PRIMARY KEY AUTOINCREMENT,
        question text NOT NULL,
        questionTypeId integer NOT NULL
    ) """

    conn = create_connection(db_file)

    if conn is not None:
        create_table(conn, create_question_table)
    else:
        print("Error could not create table")

def setup():
    '''DB Set up'''
    call_create_table(QConstants.MYDB)

def insert_question(question):
    '''Function to insert question in DB'''
    sql = ''' INSERT INTO question(question, questionTypeId) VALUES(?,?) '''
    conn = create_connection(QConstants.MYDB)
    cur = conn.cursor()
    cur.execute(sql, (question.get_question(), question.get_question_type_id()))
    conn.commit()
    return cur.lastrowid

def remove_question(question_id):
    '''Function to remove question in DB'''
    sql = ''' DELETE FROM question WHERE questionId = ?'''
    conn = create_connection(QConstants.MYDB)
    cur = conn.cursor()
    cur.execute(sql, (question_id,))
    conn.commit()

def get_questions():
    '''Function to show all qs in DB'''
    conn = create_connection(QConstants.MYDB)
    cur = conn.cursor()
    cur.execute("SELECT * FROM question")

    rows = cur.fetchall()

    for row in rows:
        print(row)
