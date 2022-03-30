'''View module command line'''

from model.question import Question, QConstants
from controller.qacontroller import insert_question, remove_question, get_questions

def handle_add():
    '''Adding a question from command line'''
    print("Enter question: ")
    qinput = input()
    question = Question(qinput, QConstants.BOOLEAN_CHOICE)
    question_id = insert_question(question)
    question.set_question_id(question_id)
    print("Question successfully added!")

def handle_remove():
    '''Removing a q from command line'''
    print("Enter questionId: ")
    qinput = input()
    remove_question(int(qinput))
    print(f"Question {qinput} successfully removed!")

def handle_view():
    '''handles view on command line'''
    print("Welcome to the exam generator!\n")
    while True:
        print("Select a choice: AddQuestion(A), RemoveQuestion(R), ShowAll(S), Quit(Q)\n")
        choice = input()
        if choice == "A":
            handle_add()
        elif choice == "R":
            handle_remove()
        elif choice == "S":
            get_questions()
        elif choice == "Q":
            exit("Thank you your data has been saved!")
        else:
            print("Invalid Choice!\n")