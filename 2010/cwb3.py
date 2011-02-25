#filename:cwb3.py
#Author: Yap Zi Xuan
#Centre No: 3024
#Description: #Append validated loan record

import datetime
import time

def LOANRESOURCE():

    try:
        #open file for reading
        loan_file = open("LOAN.DAT","w")

        #open uresource.dat to read
        uresource_file = open("URESOURCE.DAT","r")

        #skip heading line
        heading_line = uresource_file.readline()

        #initilaise ResourceNo list
        resourceno_list = []

        #read in all record numbers
        detail_lines = uresource_file.readlines()

        #loop through all records
        for resource_line in detail_lines:            

            #get ResourceNo
            resourceno = resource_line[0:5]

            #append ResourceNo to list
            resourceno_list.append(resourceno)

        valid_numRecordsBorrow = False
        while not valid_numRecordsBorrow:
            numRecordsBorrow = input("Enter number of records to be loaned: ")            
            if len(numRecordsBorrow) == 0: #presence checking
                print("field must not be empty. Try again.")            
            elif not numRecordsBorrow.isdigit(): #data type check
                print("field must only consist of integers. Try again.")    
            elif not 0 < int(numRecordsBorrow) <= 3: #range check
                print("You can only borrow up to 3 items. Try again.")    
            else:
                valid_numRecordsBorrow = True

        for entry in range(int(numRecordsBorrow)):        

            #get and validate ResourceNo
            valid_resourceno = False        
            while not valid_resourceno:
                resourceno = input("Enter resource no: ")
                if len(resourceno) == 0: #presence check
                    print("Error! Field cannot be empty!")
                elif len(resourceno) != 5: #length check
                    print("Error! Number must consist of 5 digits!")
                elif not(resourceno).isdigit(): #data type check
                    print("Error! Number must consist of 5 digits!")
                elif resourceno not in resourceno_list:
                    print("Eror! Resource does not exist.")
                else:
                    valid_resourceno = True
                #assume resource is not loaned    

            #get and valdiate StudentID
            valid_studentID = False
            while not valid_studentID:
                studentID = input("Enter student ID: ")
                if len(studentID) == 0: #presence check
                    print("Error! Field cannot be empty!")
                elif len(studentID) != 5: #length check
                    print("Error! Number must consist of 5 digits!")
                elif not studentID[0:1].upper()== 'S': #data type check
                    print("Error!first character must be an 'S'!")
                elif not studentID[1:5].isdigit():
                    print("Error! There must be 4 digits following the 'S' letter!")
                elif not 0< int(studentID[1:5])<10000:
                    print("Error! student ID must be from S0001 to S9999.")            
                else:
                    valid_studentID = True
            

            #get and validate StudentName
            valid_studentName = False
            while not valid_studentName:
                studentName = input("Enter your name: ")
                if len(studentName) == 0: #presence check
                    print("Error! Field cannot be empty!")
                elif len(studentName)> 30: #length check
                    print("Error! Number must consist not more than 30 digits!")          
                else:
                    valid_studentName = True        

            #calculate DateDueBack
            DateLoaned = (datetime.date.today())
            DateDueBack = DateLoaned + datetime.timedelta(days=7)
            
            #format date DDMMYY        
            DateDueBack = DateDueBack.strftime("%d%m%y")

            # create 'empty' evaluation        
            evaluation = " "*50        
            
            # write information to file
            loan_file.write("%5s%-5s%30s%6s%50s" % (resourceno, studentID, studentName, DateDueBack, evaluation) + "\n")
        
        #close files
        loan_file.close()
        uresource_file.close()

    except IOError:
        #display input file error
        print("Error! Reference file does not exist or is corrupted")

#main
if __name__ == "__main__":
    LOANRESOURCE()
