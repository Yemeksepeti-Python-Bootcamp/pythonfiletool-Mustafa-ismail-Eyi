#%%


from pathlib import Path
import os
from posixpath import split

import pandas as pd

from tabulate import tabulate 
import sys
import csv

class FileTool:
    

    def __init__(self, path = "",*args):
        self.path = path
        self.fields = list(args)

        if self.isFileExists():
            if self.hasFileHeaders():
                if self.isFeaturesMatches:
                    self.data = pd.read_csv(self.path, usecols=[col for col in self.fields])
                    self.userChoice()
                else:
                    print("Features do not match")
            else:
                self.data = pd.read_csv(self.path, header=0, names=[str(i) for i in range(pd.read_csv(self.path).shape[1])])
                self.userChoice()
        else:
            raise Exception("CSV file does not exist")
        



    # the main idea of being property that method is can be used like a variable
    def isFileExists(self):
        #TODO this method will be refactored with os.path.abspath() 
        """ This checks the entered file exists or not"""
        if str(self.path).find('/') == -1: # if the given path is the data's itself
            if os.path.exists(Path(os.getcwd()) / self.path):
                return 1
            else:
                return 0
        else: # if the given path is the a absolute path
            if os.path.exists(Path(os.getcwd()) / self.path): # checking the data is csv or json else return false
                if self.path.endswith(".csv") or self.path.endswith(".json"):
                    return 1
                else:
                    return 0
            else:
                return 0


    def userChoice(self):
        """ Requires the choice of user """
        __flag = True
        print("Press 1 to search the data")
        print("Press 2 to delete a record")
        print("Press 3 to append a data")
        print("Press 4 to update")
        print('Press 5 to print the data')
        print("Press 6 to export one line of data to json")
        print("Press 7 to append the data to another data")
    
        print("Press 0 to exit")
        
        while __flag:
            user_input = input("Please enter a number")
            if user_input == '1':
                self.searchData()
            elif user_input == '2':
                self.deleteData()
            elif user_input == '3':
                self.addData()
            elif user_input == '4':
                pass
            elif user_input == '5': 
                try:
                    row_n = int(input("To see all data enter \'-1\' else to see a row enter index of it"))
                    self.printData(row_n)
                except:
                    print("Please enter a number")
            elif user_input == '6':
                self.exportToJsonOne()

            elif user_input == '7':
                self.exportBulkData()

            elif user_input == '0':
                __flag = False
                print("Bye bye")
                sys.exit(0)
            
            else:
                try:
                    if int(user_input) not in range(0,8):
                        print("Please enter a number range in between 0 and 7")
                except:
                    print("Wrong character please enter a number range in between 0 and 7")
    
    def searchData(self):
        #TODO This method will search the data point
        col = input("Please enter the column name")
        value = input("Please enter the value")
        # example data[data["Style"]=="Cup"]
        try:
            print(tabulate(self.data[self.data[col]==value], headers='keys', tablefmt='psql'))
        except:
            print("Column name is not valid or value type incosistent")

    def addData(self):
        """ This method will add the data at the end
            Please Enter the values as comma seperated
            field1, field2, field3, ... fieldn
        """
        
        datas = [i for i in input("Please enter the data as comma seperated format respect to fields of the data").split(',')]
        temporary_df = pd.DataFrame(datas,columns=self.data.columns)
        try:
            self.data.append(temporary_df)
            print("Data is added")
            del temporary_df, datas
        except:
            print("datas do not match with features")

    def deleteData(self):
        ind = int(input("Enter the index of record which will be deleted"))
        try:
            self.data.drop([self.data.index[ind]]).reset_index(drop=True)
        except:
            print(f"Index is out of range. Enter the number between 0 - {len(self.data)}")
        finally:
            del ind

    @property
    def isFeaturesMatches(self):
        """ Checks the featrues matches or not"""
        features = [str(x).lower() for x in pd.read_csv(self.path).columns]
        for cols in self.fields:
            if str(cols).lower() not in features:
                return False
        return True

    def exportToJsonOne(self):
        """ export the one line of data to JSON file"""
        data_index = int(input("Enter the index of the data that you want the print as JSON"))
        while not(0 < data_index < len(self.data)):
            data_index = int(input(f"Enter the index between 0 and {len(self.data)}"))
        temporary_df = self.data.loc[[data_index]]
        temporary_df.to_json('./asdasdas.json')
        

    def exportToCSV(self,):
        """ export the whole data to csv file """
        #TODO exporting folder and the name of file needed to be identified
        to_csv_path = "".join(self.path.split('/')[:-1]) if len(self.path.split('/')) != 1 else f'./{self.data}' 
        self.data.to_csv(to_csv_path.replace('.csv','.csv'))

    def printData(self,start):
        """
        Print the data as in tabulate format
        """
        if start == -1:
            print(tabulate(self.data[:start], headers='keys', tablefmt='psql'))
        else:
            print(tabulate(self.data.loc[[start]],headers="keys",tablefmt="psql"))

    def hasFileHeaders(self, path = None):
        """
        This method checks the csv file has columns or not
        """
        if path is None:
            with open(self.path, 'r') as csvfile:
                sniffer = csv.Sniffer() # sniffer handles the header problem are there exist or not
                has_header = sniffer.has_header(csvfile.read(2048)) # 2048 is arbitrary number which is need to read 2-3 rows as bytes
                csvfile.seek(0) # set the cursor at the beginning
        else:
            with open(self.path, 'r') as csvfile:
                sniffer = csv.Sniffer() # sniffer handles the header problem are there exist or not
                has_header = sniffer.has_header(csvfile.read(2048)) # 2048 is arbitrary number which is need to read 2-3 rows as bytes
                csvfile.seek(0) # set the cursor at the beginning

        # returns boolean
        return has_header 

    def exportBulkData(self):
        dest_path = input("enter the path where you want to append the your data")
        if self.hasFileHeaders(path=dest_path):
            self.data.to_csv(dest_path, mode='a', header=False)
        else:
            self.data.to_csv(dest_path, mode='a', header=True)
    

    
    def __repr__(self) -> str:
        return f"folder path:{self.path.split('/')[:-1]} file:{self.path.split('/')[-1]} fields: {''.join(*self.fields)}" 




#%%
# test = FileTool("")

test = FileTool('./ramen-ratings.csv','Variety','Style','Country','Stars','Top Ten')

#%%
test = FileTool('./headless.csv')
# %%
import pandas as pd
from tabulate import tabulate 
data = pd.read_csv('./ramen-ratings.csv')
# %%
#print(tabulate(data[:-1], headers='keys', tablefmt='psql'))# %%
print(data.shape)
# # %%
# import pandas as pd

# [x for x in pd.read_csv('ramen-ratings.csv').columns]
# # %%

# %%
print(data.loc[[0]])
# %%
a="Style"
b="Cup"
data['Style'].drop_duplicates()
data[data["Style"]=="Cup"]
print(data.Stars.dtype)
# %%
data.info()
# %%


# %%
data
# %%
