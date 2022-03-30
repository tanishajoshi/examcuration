from model.question import Question, QConstants

from controller.qacontroller import insert_question, remove_question, get_questions

def handle_add():
    print("Enter question: ")
    qinput = input()
    question = Question(qinput, QConstants.BOOLEAN_CHOICE)
    questionId = insert_question(question)
    question.set_question_id(questionId)
    print("Question successfully added!")

def handle_remove():
    print("Enter questionId: ")
    qinput = input()
    remove_question(int(qinput))
    print(f"Question {qinput} successfully removed!")

def handle_view():
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