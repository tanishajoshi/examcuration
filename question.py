'''Class to define a question.'''
class Question:

    '''Initialization of question class.'''
    def __init__(self, ques):
        self.ques = ques

    '''Edit and replace a question.'''
    def edit(self, new_ques):
        self.ques = new_ques

    '''Delete a question.'''
    def delete(self):
        self.ques.remove()
        
    '''Return the string of the question.'''
    def get_question(self):
        return self.ques
