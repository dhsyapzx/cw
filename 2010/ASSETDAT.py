# Filename: ADDASSET.py
# Author: 
# Centre No/Index No: 
# Description: Get AV/IT asset input from user and store in text file

import datetime
import re
import os

def ADDASSET():
    try:
        exist = os.path.exists("RESOURCE.DAT")
        
        # set pattern
        AssetID_APattern = re.compile("[Aa]")
        AssetID_TPattern = re.compile("[Tt]")
        
        if exist:
            asset_file = open("RESOURCE.DAT", "r+")
            asset_file.readline()
            CurrentFile = asset_file.readlines()
            a_count = 0
            t_count = 0
            
            asset_file.seek(0)
            for line in asset_file:
                if AssetID_APattern.match(asset_file.read(1)):
                    a_count += 1
                else:
                    t_count += 1
            if t_count != 0:
                t_count -= 1
            asset_file.close()
                   
        else:
            CurrentFile = []

        asset_file = open("RESOURCE.DAT", "w+")

        # get update date
        UpdateDate = datetime.date.today()    
    
        asset_file.write(UpdateDate.strftime("%d-%m-%Y"))

        print("Total number of Assets in file is: " + str(len(CurrentFile)))
        maxAdd = 19998 - len(CurrentFile)
        valid_NumberOfAssets = False
        while not valid_NumberOfAssets:
    
            # input of NumberOfAssets
            NumberOfAssets = input("Enter number of Assets to be recorded: ")
            
            # Checking if NumberOfAssets is null
            if len(NumberOfAssets) == 0:
                print("*WARNING*" + "\n" + "AN ERROR OCCURED:" + "\n" +
                      "Number of Assets must not be empty. Try again.")
    
            # Checking that input contains only digits
            elif not NumberOfAssets.isdigit():
                print("*WARNING*" + "\n" + "AN ERROR OCCURED:" + "\n" +
                      "Number of Assets must only consist of integers. Try again.")
    
            # Checking range of input 0 < input < 9999
            elif not 0 < int(NumberOfAssets) <= maxAdd:
                print("*WARNING*" + "\n" + "AN ERROR OCCURED:" + "\n" +
                      "Number of Assets must be within 1 to 9999. Try again.")
    
            else:
                valid_NumberOfAssets = True

        NumberOfAssets = int(NumberOfAssets)
        TotalAssets = NumberOfAssets + len(CurrentFile)
        asset_file.write(str(TotalAssets)+"\n")

        if exist:
            for each in CurrentFile:
                asset_file.write(each)
        else:
            a_count = 0
            t_count = 0

        for entry in range(int(NumberOfAssets)):

            # showing user entry no.
            print("\n" + "Entry number: " + str(entry+1) + "\n")
            print("current ID for \'A\': " + str(a_count+1))
            print("current ID for \'T\': " + str(t_count+1))

            # get and validate AssetID
            valid_AssetID = False
        
            while not valid_AssetID:

                # input of AssetID
                AssetID = input("Enter Asset ID: ")

                # Checking if input is null
                if len(AssetID) == 0:
                    print("*WARNING*" + "\n" + "AN ERROR OCCURED:" + "\n" +
                          "Asset ID must not be empty. Try again.")

                # Checking that input has length = 5
                elif not len(AssetID) == 5:
                    print("*WARNING*" + "\n" + "AN ERROR OCCURED:" + "\n" +
                          "Asset ID must be exactly 5 digits. Try again.")
                elif not AssetID[1:6].isdigit():
                    print("*WARNING*" + "\n" + "AN ERROR OCCURED:" + "\n" +
                          "Last 4 characters of Asset ID must be integers. Try again.")

                else:
                    if AssetID_APattern.match(AssetID):
                        if not AssetID[1:6] == str(a_count+1).zfill(4):
                            print("*WARNING*" + "\n" + "AN ERROR OCCURED:" + "\n" +
                                  "Asset ID entered is not in order. Try again.")
                        else:
                            a_count+=1
                            AssetID = AssetID.upper()
                            valid_AssetID = True
                    elif AssetID_TPattern.match(AssetID):
                        if not AssetID[1:6] == str(t_count+1).zfill(4):
                            print("*WARNING*" + "\n" + "AN ERROR OCCURED:" + "\n" +
                                  "Asset ID entered is not in order. Try again.")
                        else:
                            t_count+=1
                            AssetID = AssetID.upper()
                            valid_AssetID = True
                    else:
                        print("*WARNING*" + "\n" + "AN ERROR OCCURED:" + "\n" +
                              "First letter of AssetID has to be A or T. Try again.")

            # get and validate Description
            valid_Description = False
            while not valid_Description:
                Description = input("Enter Asset Description: ")
                
                if not 0 < len(Description) <= 30:
                    print("*WARNING*" + "\n" + "AN ERROR OCCURED:" + "\n" +
                          "Description is either empty or has more than 30 characters. Try again.")
                else:
                    valid_Description = True

            # get and validate DatePurchased
            valid_DatePurchased = False
            DatePurchased_Pattern = re.compile("^[0-9]{4}[-][0-9]{2}[-][0-9]{2}$")
            while not valid_DatePurchased:
                DatePurchased = input("Enter purchased date of Asset (YYYY-MM-DD): ")
                if len(DatePurchased) != 10:
                    print("*WARNING*" + "\n" + "AN ERROR OCCURED:" + "\n" +
                         "Data of Purchase is either empty or not exactly 10 digits. Try again.")
                elif not DatePurchased_Pattern.match(DatePurchased):
                    print("*WARNING*" + "\n" + "AN ERROR OCCURED:" + "\n" +
                          "Date Purchased should consist of 10 characters in the format(YYYY-MM-DD).")
                           
                elif datetime.datetime.strptime(DatePurchased, "%Y-%m-%d") > (datetime.datetime.today()):
                    print("*WARNING*" + "\n" + "AN ERROR OCCURED:" + "\n" +
                          "Invalid Date. Try again.")

                else:
                    try:
                        datetime.datetime.strptime(DatePurchased, "%Y-%m-%d")
                        valid_DatePurchased = True
                    except ValueError:
                         print("*WARNING*" + "\n" + "AN ERROR OCCURED:" + "\n" +
                               "Invalid Date. Try again.")

           # get and validate Status
            valid_Status = False

            Status_Pattern = re.compile("[AaLlFfCc]")

            while not valid_Status:
                Status = input("Enter 'A' if asset is available; 'L' if asset is On Loan; 'F' is asset is Faulty; 'C' is asset is Condemned: ")
                if len(Status) != 1:
                    print("*WARNING*" + "\n" + "AN ERROR OCCURED:" + "\n" +
                          "Only 1 character: 'A', 'L', 'F', or 'C' is allowed. Try again.")
                elif not Status_Pattern.match(Status):
                    print("*WARNING*" + "\n" + "AN ERROR OCCURED:" + "\n" +
                          "Only 'A', 'L', 'F', or 'C' is allowed. Try again.")
                else:
                    valid_Status = True
                    Status = Status.upper()

                # write information to file
                asset_file.write("%5s%-30s%10s%1s" % (AssetID, Description, DatePurchased, Status) + "\n")

                if not str(entry+1) == str(NumberOfAssets):
                    print("Data saved. Proceeding to next entry." + "\n")
                else:
                    print("Data saved." + "\n")

        # close file
        asset_file.close()
        print("All data saved.")

    except IOError:
        print("*WARNING*" + "\n" + "AN ERROR OCCURED:" + "\n" +
              "Error! Unable to create and write to file.")

# main program
if __name__ == "__main__":
    ADDASSET();                      
