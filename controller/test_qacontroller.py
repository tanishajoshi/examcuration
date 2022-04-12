"""Tests for controller module."""
from model.question import Question, QConstants
from controller.qacontroller import insert_question, remove_question, get_questions, setup

def clear_questions():
    '''Utility function to remove all questions from DB.'''
    questions = get_questions()
    for question in reversed(questions):
        question_id = question[0]
        print(question_id)
        remove_question(question_id)
    questions = get_questions()
    print("Printing DB")
    print(questions)

def test_add_question():
    '''Tests that adding a question returns it as the most recently added question.'''
    sample_q = Question("What is my name?", QConstants.FREE_RESPONSE, "Johhny Bravo")
    setup()
    question_id = insert_question(sample_q)
    sample_q.set_question_id(question_id)

    questions = get_questions()
    check_q = questions[len(questions)-1]
    assert check_q[0] == sample_q.get_question_id()
    assert check_q[1] == sample_q.get_question()

def test_remove_question():
    '''Test for verifying that questions can be removed from the database.'''
    sample_q = Question("What is my name?", QConstants.FREE_RESPONSE, "Johhny Bravo")
    setup()
    question_id = insert_question(sample_q)
    sample_q.set_question_id(question_id)
    questions = get_questions()
    remove_question(sample_q.get_question_id())

    questions = get_questions()
    check_q = questions[len(questions)-1]
    assert check_q[0] == sample_q.get_question_id()
    assert check_q[1] == sample_q.get_question()
