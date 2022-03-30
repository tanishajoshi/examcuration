import sqlite3
from sqlite3 import Error
from model.question import Question, QConstants

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    return conn

def call_create_table(db_file):
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
    call_create_table(QConstants.MYDB)

def insert_question(question):
    sql = ''' INSERT INTO question(question, questionTypeId) VALUES(?,?) '''
    conn = create_connection(QConstants.MYDB)
    cur = conn.cursor()
    cur.execute(sql, (question.get_question(), question.get_question_type_id()))
    conn.commit()
    return cur.lastrowid

def remove_question(questionId):
    sql = ''' DELETE FROM question WHERE questionId = ?'''
    conn = create_connection(QConstants.MYDB)
    cur = conn.cursor()
    cur.execute(sql, (questionId,))
    conn.commit()

def get_questions():
    conn = create_connection(QConstants.MYDB)
    cur = conn.cursor()
    cur.execute("SELECT * FROM question")

    rows = cur.fetchall()

    for row in rows:
        print(row)

