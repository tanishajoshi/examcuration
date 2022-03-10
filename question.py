'''Class to define a question.'''
class Question:

    '''Initialization of question class.'''
    def __init__(self, ques, ans):
        self.ques = ques
        self.ans = ans

    '''Edit and replace a question.'''
    def edit(self, new_ques, new_ans):
        self.ques = new_ques
        self.ans = new_ans;

    '''Delete a question.'''
    def delete(self):
        self.ques.remove()
        
    '''Return the string of the question.'''
    def get_question(self):
        return self.ques
    
    '''Return the string of the answer.'''
    def get_answer(self):
        return self.ans
