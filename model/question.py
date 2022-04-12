"""This is the question class"""
# disabling:
# R0903: Too few public methods
# pylint: disable=R0903
class QConstants:
    '''QConstants Class'''
    MYDB = "qadb"
    FREE_RESPONSE = 1
    MULTIPLE_CHOICE = 2
    BOOLEAN_CHOICE = 3 #Default question type for now

class Question:
    '''Question Class'''
    def __init__(self, question, question_type_id, question_answer=0):
        '''Initialization of question class.'''
        self.question_id = None
        self.question = question
        self.question_type_id = question_type_id
        #TODO: Ensure question answer format is appropriate for question type
        self.question_answer = question_answer # Default to NONE if no right answer or none provided

    def get_question_id(self):
        '''Return question id'''
        return self.question_id

    def get_question(self):
        '''Return the question.'''
        return self.question

    def get_question_type_id(self):
        '''Return question type id'''
        return self.question_type_id

    def set_question_id(self, question_id):
        '''Set question id'''
        self.question_id = question_id

    def get_answer(self):
        return self.question_answer
    
    def update_answer(self, new_answer):
        self.question_answer = new_answer
