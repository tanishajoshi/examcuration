''' File containing graphical user interface. '''
# disabling:
# pylint: disable=E0401
# pylint: disable=W0105
# pylint: disable=W0401
# pylint: disable=R0915
# pylint: disable=C0103
# pylint: disable=W0614
# pylint: disable=C0303
import tkinter.messagebox
from tkinter import *
from model.question import Question
from controller.qcontroller import QController
from setup import setup
#root = tk.Tk()
#root.geometry("200x100")

#textExample = tk.Entry(root)

''' Beginning state of user interface. '''
def start():
    """start method"""

    print("CAME HERE")
    ''' Create data table for questions and answers to be stored. '''
    setup()
    qcontroller = QController("sqlite")

    ''' Create window for gui. '''
    ui=Tk()
    ui.title("Please make a selection")
    #questionEntry = ui.Entry(root)


    ui.geometry('300x500')


    ''' Functions of add, edit, and remove buttons. '''
    def add():
        ''' New window created when the add button is clicked. '''
        add_question_window = Tk()
        add_question_window.title("Add Question")
        add_question_window.geometry('600x200')

        ''' Function that adds questions. '''
        def add_question():
            if len(question_entry.get()) == 0:
                tkinter.messagebox.showinfo('Enter a question', 'Please enter a question')
            elif len(answer_entry.get()) == 0:
                tkinter.messagebox.showinfo('Enter an answer', 'Please enter an answer')
            else:
                question = Question(question_entry.get(), 1)
                question_id = qcontroller.insert_question(question)
                question.set_question_id(question_id)
                tkinter.messagebox.showinfo('add question', 'Question and answer have been stored!')

        ''' Text bar to enter questions and answers. '''
        Label(add_question_window,
              text='Question:',
              font=("Helvetica", 15)).place(relx = 0,
              rely = 0.1,
              anchor='w')
        question_entry = Entry(add_question_window, width=80)
        question_entry.place(relx = 0.56, rely = 0.1, anchor='center')

        ''' Text bar to enter answers. '''
        Label(add_question_window,
              text='Answer:',
              font=("Helvetica", 15)).place(relx = 0,
              rely = 0.3,
              anchor='w')
        answer_entry = Entry(add_question_window, width=82)
        answer_entry.place(relx = 0.55, rely = 0.3, anchor='center')

        ''' Text bar to enter tags. '''
        Label(add_question_window, text='Tags:',
        font=("Helvetica", 15)).place(relx = 0,
        rely = 0.5,
        anchor='w')
        tag_entry = Entry(add_question_window, width=86)
        tag_entry.place(relx = 0.53, rely = 0.5, anchor='center')

        ''' Add question, edit question, view questions and delete question buttons. '''
        add_button=Button(add_question_window,text="Add Question",
        font=("Helvetica", 10),
        width=15,height=3,
        command=add_question,
        bg='white')
        add_button.place(x=250,y=125)


    def edit():
        ''' New Window created when the edit button is clicked. '''
        edit_question_window = Tk()
        edit_question_window.title("Edit Question")
        edit_question_window.geometry('600x300')
        def edit_question():
            if len(question_id_entry.get()) == 0:
                tkinter.messagebox.showinfo('Enter ID message', 'Please enter a question ID')
            else:
                tkinter.messagebox.showinfo('edit message', 'Your question has been changed!')

        ''' Text bar to find questions. '''
        Label(edit_question_window,
        text='Question ID:',
        font=("Helvetica", 15)).place(relx = 0,
        rely = 0.1,
        anchor='w')
        question_id_entry = Entry(edit_question_window, width=75)
        question_id_entry.place(relx = 0.58, rely = 0.1, anchor='center')

        ''' Text bar to enter questions and answers. '''
        Label(edit_question_window, text='Question:',
        font=("Helvetica", 15)).place(relx = 0,
        rely = 0.3,
        anchor='w')
        question_entry = Entry(edit_question_window, width=80)
        question_entry.place(relx = 0.56, rely = 0.3, anchor='center')

        ''' Text bar to enter answers. '''
        Label(edit_question_window, text='Answer:',
        font=("Helvetica", 15)).place(relx = 0,
        rely = 0.5,
        anchor='w')
        answer_entry = Entry(edit_question_window, width=82)
        answer_entry.place(relx = 0.55, rely = 0.5, anchor='center')

        ''' Change button. '''
        change_button=Button(edit_question_window,text="Change Question/Answer",
        font=("Helvetica", 10),
        width=20,
        height=5,
        command=edit_question,
        bg='white')
        change_button.place(x=225,y=200)

    def delete():
        ''' New window created when the delete button is clicked. '''
        delete_question_window = Tk()
        delete_question_window.title("Delete Question")
        delete_question_window.geometry('600x200')

        '''Delete function. '''
        def delete_question():
            if len(question_id_entry.get()) == 0:
                tkinter.messagebox.showinfo('Enter ID message', 'Please enter a question ID')
            else:
                qcontroller.remove_question(question_id_entry.get())
                tkinter.messagebox.showinfo('delete message', 'Your question has been deleted!')

        ''' Text bar to find questions. '''
        Label(delete_question_window,
        text='Question ID:',
        font=("Helvetica", 15)).place(relx = 0,
        rely = 0.1,
        anchor='w')
        question_id_entry = Entry(delete_question_window, width=75)
        question_id_entry.place(relx = 0.58, rely = 0.1, anchor='center')

        ''' Delete button. '''
        delete_button=Button(delete_question_window,
        text="Delete",
        font=("Helvetica", 10),
        width=20,
        height=5,
        command=delete_question,
        bg='white')
        delete_button.place(x=225,y=75)

    ''' View all questions. '''
    def view():
        tkinter.messagebox.showinfo('Show questions', qcontroller.get_questions())

    ''' Add question, edit question, view questions and delete question buttons. '''
    add_button=Button(ui,
    text="Add Question",
    font=("Helvetica", 10),
    width=15,
    height=5,
    command=add,
    bg='white')
    add_button.place(x=90,y=25)

    edit_button=Button(ui,
    text="Edit Question",
    font=("Helvetica", 10),
    width=15,
    height=5,
    command=edit,
    bg='white')
    edit_button.place(x=90,y=125)

    delete_button=Button(ui,
    text="Delete Question",
    font=("Helvetica", 10),
    width=15,
    height=5,
    command=delete,
    bg='white')
    delete_button.place(x=90,y=225)

    view_button=Button(ui,
    text="View Questions",
    font=("Helvetica", 10),
    width=15,
    height=5,
    command=view,
    bg='white')
    view_button.place(x=90,y=325)

    ''' Loop that runs gui until closed out. '''
    ui.mainloop()
