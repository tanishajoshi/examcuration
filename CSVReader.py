import csv
from question import Question

'''Read and output a set of questions from the CSV file'''
def readFromFile():
    print("Hello");

'''Write a question to a CSV file'''
def writeToFile():
    cont = True;
    while cont: 
        ##Get input for question and answer
        print("Please enter a question.")
        q_input = input();
        print("Please enter a solution. Leave blank for no answer.")
        a_input = input();
        print(q_input, a_input);

        ##Encapsulate in question class
        quest = Question(q_input, a_input);


        ##Write question class object to CSV
        # name of csv file 
        filename = "Questions.csv"

        fields = ['Question', 'Answer'] 
        rows = [[quest.get_question(), quest.get_answer()]]
        
        # writing to csv file 
        with open(filename, 'w') as csvfile: 
            # creating a csv writer object 
            csvwriter = csv.writer(csvfile) 
                
            # writing the fields 
            csvwriter.writerow(fields) 
                
            # writing the data rows 
            csvwriter.writerows(rows)

        ##Ask user whether they want to add another question or not
        print("Continue? y/n")
        c_input = input();
        if (c_input != 'y' and c_input != 'Y'):
            print("Exiting!")
            cont = False;

'''Generate a CSV file.'''
def getCSVFile():
    # field names 
    fields = ['Name', 'Branch', 'Year', 'CGPA'] 
    
    # data rows of csv file 
    rows = [ ['Nikhil', 'COE', '2', '9.0'], 
         ['Sanchit', 'COE', '2', '9.1'], 
         ['Aditya', 'IT', '2', '9.3'], 
         ['Sagar', 'SE', '1', '9.5'], 
         ['Prateek', 'MCE', '3', '7.8'], 
         ['Sahil', 'EP', '2', '9.1']] 
    
    # name of csv file 
    filename = "university_records.csv"
    
    # writing to csv file 
    with open(filename, 'w') as csvfile: 
        # creating a csv writer object 
        csvwriter = csv.writer(csvfile) 
            
        # writing the fields 
        csvwriter.writerow(fields) 
            
        # writing the data rows 
        csvwriter.writerows(rows)
