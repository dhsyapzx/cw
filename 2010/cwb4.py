#cwb4.py

def LOANREPORT():
    try:
        #open files for reading
        loan_file = open("LOAN.DAT","r")        
        uresource_file = open("URESOURCE.DAT","r")

        #initialise a dictionary
        dictLoan = {}

        #initialise lists
        loanList = []
        megaList = []
        dateList = []
        finalList = []

        #get resource details
        detail_lines = loan_file.readlines()
        detail2_lines = uresource_file.readlines()

        #loop through each resource
        for record_line in detail_lines:
            
            #clean each record line
            record_line = record_line.rstrip("\n")

            #get and store record info from loan file
            resourceNo = record_line[0:5]
            studentID = record_line[5:10]
            studentName = record_line[10:40]
            DateDueBack = record_line[40:46]
            
            if DateDueBack not in dateList:
                dateList.append(DateDueBack)

            #get resource title and resource type from uresource file           
            for record2_line in detail2_lines:
                record2_line = record2_line.rstrip("\n")
                #check if current resource no is present in both loan and uresource file
                if (resourceNo == record2_line[0:5]):
                    resourceTitle = record2_line[5:35]
                    resourceType = record_line[41:]
                    #rewrite output for resource type
                    if resourceType == "C":
                        resourceType = "CD"
                    else:
                        resourceType = "DVD"
                    #proceed once matching details are located
                    break
                else:
                    continue     

            #append to loan list
            loanList = [DateDueBack,resourceNo,resourceTitle,resourceType,studentID,studentName]
            
            #append to a list of lists (but not final list yet)
            megaList.append(loanList)

            #set loan list to empty again to store next cycle's data
            loanList = list()

        #compare dates in megaList and dateList
        for date in dateList:
            for loan in megaList:
                if (date == loan[0]):
                    del loan[0]
                    finalList.append(loan)
            dictLoan[date] = finalList
            #make finalList empty again to store loan data in next cycle
            finalList = list()                                       

        #print contents of dictionary
        for k, v in dictLoan.items():
            #print date due back
            print(k)
            #loop through list of resources
            for i in range(len(v)):
                #loop through list of loan resource info(resource no, title, etc)
                for j in range(len(v[i])): 
                    #display each loan resource info(resource no, title, etc) on same line
                    print(v[i][j], end = " ")
                #go to new line to start next loan resource record    
                print()
            #number of resources due on that day    
            print("number of resources: ",len(v))

        #close files
        loan_file.close()
        uresource_file.close()            
        
    except IOError:
            #display input file error
            print("Error! Reference file does not exist or is corrupted.")
            
#main
if __name__ == "__main__":
    LOANREPORT()        
