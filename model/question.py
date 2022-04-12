"""This is the question model."""

class Question:
    """
    A class to represent a Question.

    Attributes
    ----------
    question : str
        The text of the question.
    questionTypeId: int
        The type of the question.

    """
    def __init__(self, question, question_type_id):
        self.question_id = None
        self.question = question
        self.question_type_id = question_type_id

    def __str__(self):
        sobj = f"question_id: {self.question_id}\n"
        sobj += f"question: {self.question}\n"
        sobj += f"question_type_id: {self.question_type_id}"
        return sobj

    def get_question_id(self):
        """Get a question id."""
        return self.question_id

    def get_question(self):
        """Get a question."""
        return self.question

    def get_question_type_id(self):
        """Get a question type id"""
        return self.question_type_id

    def set_question_id(self, question_id):
        """Set a question id."""
        self.question_id = question_id