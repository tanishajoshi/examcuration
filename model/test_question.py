'''Module for testing question.py.'''
from model.question import Question, QConstants

def test_generate_question():
    '''Tests generating a question'''
    sample_q = Question("What is my name?", 2, "Johhny Bravo")

    assert (isinstance(sample_q, Question))

def test_update_answer():
    '''Tests updating an answer to an already generated question'''
    sample_q = Question("What is my name?", QConstants.FREE_RESPONSE, "Johhny Bravo")
    sample_q.update_answer("Courage the Cowardly Dog")

    assert sample_q.get_answer() == "Courage the Cowardly Dog"

def test_set_question_id():
    '''Tests setting a question ID'''
    sample_q = Question("What is my name?", QConstants.FREE_RESPONSE, "Johhny Bravo")
    sample_q.set_question_id(24)
    assert sample_q.get_question_id() == 24
    sample_q.set_question_id(sample_q.get_question_id() + 24)
    assert sample_q.get_question_id() == 48

def test_question_type():
    '''Tests initialization of question properly sets Question Type'''
    sample_q = Question("What is my name?", QConstants.FREE_RESPONSE, "Johhny Bravo")
    assert sample_q.get_question_type_id() == QConstants.FREE_RESPONSE
