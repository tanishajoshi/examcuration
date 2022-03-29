class Question:
    '''Class to define a question.'''

    def __init__(self, ques, ans):
        '''Initialization of question class.'''
        self.ques = ques
        self.ans = ans

    def edit(self, new_ques, new_ans):
        '''Edit and replace old question with a new question.'''
        self.ques = new_ques
        self.ans = new_ans

    def delete(self):
        '''Delete a question.'''
        self.ques.remove()

    def get_question(self):
        '''Return the string of the question.'''
        return self.ques

    def get_answer(self):
        '''Return the string of the answer.'''
        return self.ans
