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

def get_question(question_id):
    '''Gets a question based on ID'''
    questions = get_questions()
    for question in questions:
        if (question[0] == question_id):
            return question
    return None

def update_question(question_id):
    '''Removes a question by ID.'''
    print("Functionality not implemented!")

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
    clear_questions()
    #Add a first question
    sample_q = Question("What is my name?", QConstants.FREE_RESPONSE, "Johhny Bravo")
    setup()
    question_id = insert_question(sample_q)
    sample_q.set_question_id(question_id)
    #Add a second question
    sample_q2 = Question("What is my address?", QConstants.FREE_RESPONSE, "20 N Grand Blvd")
    question_id2 = insert_question(sample_q2)
    sample_q2.set_question_id(question_id2)
    questions = get_questions()
    print(len(questions))
    remove_question(sample_q.get_question_id())

    questions = get_questions()
    print(len(questions))
    check_q = questions[0]
    print(questions)
    assert check_q[0] == sample_q2.get_question_id()
    assert check_q[1] == sample_q2.get_question()

def test_get_question():
    '''Test for verifying question getter.'''
    clear_questions()
    sample_q = Question("What is my name?", QConstants.FREE_RESPONSE, "Johhny Bravo")
    sample_q2 = Question("What is my address?", QConstants.BOOLEAN_CHOICE, "20 N Grand Blvd")
    setup()
    question_id = insert_question(sample_q)
    sample_q.set_question_id(question_id)
    question_id = insert_question(sample_q2)
    sample_q2.set_question_id(question_id)

    assert get_question(question_id) == (question_id, 'What is my address?', 3)

def test_update_question():
    '''Test for verifying that updating a question updates it.'''
    sample_q = Question("What is my name?", QConstants.FREE_RESPONSE, "Johhny Bravo")
    setup()
    question_id = insert_question(sample_q)
    sample_q.set_question_id(question_id)
    sample_q.update_answer("Courage the Cowardly Dog")
    update_question(sample_q)
