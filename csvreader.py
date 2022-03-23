'''Module for reading and writing to a CSV file'''
import csv
from question import Question

def read_file():
    '''Read and output a set of questions from the CSV file'''
    print("Hello")

def write_file():
    '''Write a question to a CSV file'''
    cont = True
    while cont:
        ##Get input for question and answer
        print("Please enter a question.")
        q_input = input()
        print("Please enter a solution. Leave blank for no answer.")
        a_input = input()
        print(q_input, a_input)

        ##Encapsulate in question class
        quest = Question(q_input, a_input)

        ##Write question class object to CSV
        ##name of csv file
        filename = "Questions.csv"

        fields = ['Question', 'Answer']
        rows = [[quest.get_question(), quest.get_answer()]]

        ##writing to csv file
        with open(filename, 'w', encoding='UTF-8') as csvfile:
            ##creating a csv writer object
            csvwriter = csv.writer(csvfile)

            ##writing the fields
            csvwriter.writerow(fields)

            ##writing the data rows
            csvwriter.writerows(rows)

        ##Ask user whether they want to add another question or not
        print("Continue? y/n")
        c_input = input()
        if c_input not in ('y', 'Y'):
            print("Exiting!")
            cont = False
