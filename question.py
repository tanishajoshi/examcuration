#Class to define a question
class Question:

    # initialization of question class
    def __init__(self, ques):
        self.ques = ques
    
    # function to edit and replace a question
    def edit(self, new_ques):
        self.ques = new_ques
	
    # function to delete a question	
    def delete(self):
        self.ques.remove()
