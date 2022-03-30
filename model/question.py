'''Class to define a question.'''

"""
CREATE TABLE `question` (
  `questionId` int NOT NULL AUTO_INCREMENT,
  `question` varchar(1024) NOT NULL,
  `questionTypeId` int NOT NULL,
  `createDate` datetime NOT NULL,
  `updateDate` datetime NOT NULL,
  PRIMARY KEY (`questionId`),
  KEY `questionTypeId_idx` (`questionTypeId`),
  CONSTRAINT `questionTypeId` FOREIGN KEY (`questionTypeId`) REFERENCES `question_type` (`questionTypeId`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
"""


class QConstants:
    '''Class QConstants. ''' 
    MYDB = "qadb"
    FREE_RESPONSE = 1
    MULTIPLE_CHOICE = 2
    BOOLEAN_CHOICE = 3


class Question:
    def __init__(self, question, questionTypeId):
        '''Initialization of question class.'''
        self.questionId = None
        self.question = question
        self.questionTypeId = questionTypeId

    def get_question_id(self):
        '''Return question id'''
        return self.questionId
        
    def get_question(self):
        '''Return the question.'''
        return self.question
    
    def get_question_type_id(self):
        return self.questionTypeId
    
    def set_question_id(self, questionId):
        '''Set question id'''
        self.questionId = questionId
