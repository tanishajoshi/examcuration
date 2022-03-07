class Question:
	'Class to define a question in database'
	def __init__(self, ques):
		self.ques = ques
	def edit(self, new_ques):
		self.ques = new_ques
	def delete(self):
		self.ques.remove()
