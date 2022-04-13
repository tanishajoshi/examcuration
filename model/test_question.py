'''Module for testing question.py.'''
from model.question import Question

def test_generate_question():
    '''Tests generating a question'''
    sample_q = Question("What is my name?", 1)

    assert isinstance(sample_q, Question)

def test_set_question_id():
    '''Tests setting a question ID'''
    sample_q = Question("What is my name?", 1)
    sample_q.set_question_id(24)
    assert sample_q.get_question_id() == 24
    sample_q.set_question_id(sample_q.get_question_id() + 24)
    assert sample_q.get_question_id() == 48

def test_question_type():
    '''Tests initialization of question properly sets Question Type'''
    sample_q = Question("What is my name?", 1)
    assert sample_q.get_question_type_id() == 1
