'''Module for testing free response.'''
from freeresponse import FreeResponse
from question import Question

def test_create_freeresponse():
    '''Test creation of a free response question'''
    sample_q = Question("What is my name?", 1)
    sample_q.set_question_id(1)
    sample_a = FreeResponse(sample_q.get_question_id(), "Johnny Bravo")

    assert sample_a.get_question_id() == sample_q.get_question_id()
    assert isinstance(sample_a, FreeResponse)
    assert sample_a.get_answer() == "Johnny Bravo"
