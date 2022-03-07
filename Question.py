class Question:
	'Class to define a question in database'
	def __init__(self, ques):
		self.ques = ques
	def edit(self, newQues):
		self.ques = newQues
	def delete(self):
		self.ques.remove()
