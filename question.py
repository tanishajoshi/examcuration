'''Class to define a question.'''
class Question:

    '''Initialization of question class.'''
    def __init__(self, ques):
        self.ques = ques

    '''Function to edit and replace a question.'''
    def edit(self, new_ques):
        self.ques = new_ques

    '''Function to delete a question.'''
    def delete(self):
        self.ques.remove()
