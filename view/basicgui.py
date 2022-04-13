''' File containing graphical user interface. '''
# disabling:
# pylint: disable=E0001
import tkinter.messagebox
from tkinter import *
from model.question import Question, QConstants
from controller.qacontroller import insert_question, remove_question, get_questions, setup

''' Beginning state of user interface. '''
def start():
    ''' Create data table for questions and answers to be stored. '''
    setup()

    ''' Create window for gui. '''
    ui=Tk() 
    ui.geometry('1000x400') 

    ''' Functions of add, edit, and remove buttons. '''
    def add():
        if len(question_entry.get()) == 0:
            tkinter.messagebox.showinfo('Enter a question', 'Please enter a question')
        elif len(answer_entry.get()) == 0:
            tkinter.messagebox.showinfo('Enter an answer', 'Please enter an answer')
        else:
            question = Question(questionEntry.get(), QConstants.FREE_RESPONSE)
            question_id = insert_question(question)
            question.set_question_id(question_id)
            tkinter.messagebox.showinfo('add question', 'Question and answer have been stored!')

    def edit():
        if len(questionIdEntry.get()) == 0:
        tkinter.messagebox.showinfo('Enter ID message', 'Please enter a question ID')
        else:
            tkinter.messagebox.showinfo('edit message', 'Your question has been changed!')

    def delete():
        if len(question_id_entry.get()) == 0:
            tkinter.messagebox.showinfo('Enter ID message', 'Please enter a question ID')
        else: 
            remove_question(questionIdEntry.get())
            tkinter.messagebox.showinfo('delete message', 'Your question has been deleted!') 

    def view():
        tkinter.messagebox.showinfo('Show questions', get_questions()) 

    ''' Text bar to enter questions and answers. '''
    Label(ui, text='Question:').grid(row=0)
    question_entry = Entry(ui, width=150)
    question_entry.grid(row=0, column=2)

    ''' Text bar to enter answers. '''
    Label(ui, text='Answer:').grid(row=1) 
    answer_entry = Entry(ui, width=150)
    answer_entry.grid(row=1, column=2)

    ''' Text bar to search for question ids. ''' 
    Label(ui, text='Question ID:').grid(row=2) 
    question_id_entry = Entry(ui, width=150)
    question_id_entry.grid(row=2, column=2)	

    ''' Add question, edit question, view questions and delete question buttons. '''    
    add_button=Button(ui,text="Add Question", width=20,height=5,command=add)
    add_button.place(x=100,y=250)

    edit_button=Button(ui,text="Edit Question", width=20,height=5,command=edit)
    edit_button.place(x=300,y=250)

    delete_button=Button(ui,text="Delete Question", width=20,height=5,command=delete)
    delete_button.place(x=500,y=250)

    view_button=Button(ui,text="View Questions", width=20,height=5,command=view)
    view_button.place(x=700,y=250)
	
    ''' Loop that runs gui until closed out. '''
    ui.mainloop()
