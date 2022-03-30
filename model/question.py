"""This is the question class"""

class QConstants:
    '''QConstants Class'''
    MYDB = "qadb"
    #FREE_RESPONSE = 1
    #MULTIPLE_CHOICE = 2
    BOOLEAN_CHOICE = 3 #Default question type for now

class Question:
    '''Question Class'''
    def __init__(self, question, question_type_id):
        '''Initialization of question class.'''
        self.question_id = None
        self.question = question
        self.question_type_id = question_type_id

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
