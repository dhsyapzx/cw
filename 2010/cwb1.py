#filename:cwb1.py
#Author: Yap Zi Xuan
#Centre No/Index No: 3024
#Description: Read data from RESOURCE.DAT, format and output to screen

import time

def DISPLAYRESOURCE():

    try:
        #open file for reading
        resource_file = open("RESOURCE.DAT", "r")
        
        #read in first line (creation date and number of records)
        heading_line = resource_file.readline()
        heading_line = heading_line.rstrip("\n")
        
        #store Creation and number of records
        creation_date = heading_line[:10]
        num_records = heading_line[10:]
        
        #display heading lines with creation date and number of records
        print("Creation Date: " + creation_date)
        print("#Records: " + num_records)
        #display subheadings
        print("{0:13s}{1:17s}{2:35s}{3}".format ("Resource No", "Resource Type", "Title", "Date Acquired"))
        print("-"*75)
        
        #read in all record detail lines
        detail_lines = resource_file.readlines()
        
        #loop through number of records
        for record_line in detail_lines:
            
            #read records detail line
            record_line = record_line.rstrip("\n")
            
            #store resource no, title, date acquired and resource type
            resource_no = record_line[0:6]
            title = record_line[6:35]
            date_acquired = record_line[35:41]
            resource_type = record_line[41:]

            
            #format date from DDMMYY to DDMMYYYY
            date_acquired = time.strptime(date_acquired, "%d%m%y")
            date_acquired = time.strftime("%d-%m-%Y", date_acquired)
            
            #format and display record detail line
            print("{0:13s}{1:17s}{2:35s}{3}".format (resource_no, resource_type, title, date_acquired))
            
        #close file
        resource_file.close()    

    except IOError:
        #display input file error
        print("Error! Input file does not exist or is corrupted!")

#main
if __name__ == "__main__":
    DISPLAYRESOURCE()
