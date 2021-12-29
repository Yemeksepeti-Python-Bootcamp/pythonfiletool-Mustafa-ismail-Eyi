#%%

#TODO need a csv test data

from pathlib import Path
import os
from posixpath import split
import pandas as pd
import sys

class FileTool:
    

    def __init__(self, path = None, *args) -> None:
        self.path = path
        self.fields = list(args)
        self.userChoice()
        if self.isFileExists:
            if self.isFeaturesMatches(args):
                self.data = pd.read_csv(self.path, usecols=[str(col).lower() for col in self.fields])
            else:
                print("Features do not match")
        



    # the main idea of being property that method is can be used like a variable
    @property
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
        flag = True
        #TODO below the user choices will be in english
        print("Aramak için 1 e basın")
        print("silme için 2 ye basın")
        print("eklemek için 3 e basın")
        print("güncelleme için 4 basın")
        print("çıkmak için 0 a basın")
        
        while flag:
            user_input = input("Lütfen Seçim Yapınız")
            if user_input == '1':
                print("Press \"1\" to search data")
                
            elif user_input == '2':
                pass
            elif user_input == '3':
                print("Press \"3\" to add data")
                self.addData()

            elif user_input == '4':
                pass
            elif user_input == '0':
                print("Bye bye")
                sys.exit(0)
            else:
                try:
                    if int(user_input) not in range(0,5):
                        print("Please enter a number range in between 0 and 5")
                except:
                    print("Wrong character please a number range in between 0 and 5")
    
    def searchData(self):
        #TODO This method will search the data point
        datas = [i for i in input("Please enter the data as comma seperated format respect to fields of the data").split(',')]

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


    @property
    def isFeaturesMatches(self,args):
        """ Checks the featrues matches or not"""
        for cols in args:
            if cols not in pd.read_csv(self.path).columns:
                return False
        return True

    def exportToJson(self):
        """ export the one line of data to JSON file"""
        pass

    def exportToCSV(self,):
        """ export the whole data to csv file """
        #TODO exporting folder and the name of file needed to be identified
        to_csv_path = "".join(self.path.split('/')[:-1]) if len(self.path.split('/')) != 1 else f'./{self.data}' 
        self.data.to_csv(to_csv_path.replace('.csv','.csv'))


    def __repr__(self) -> str:
        return f"folder path:{self.path.split('/')[:-1]} file:{self.path.split('/')[-1]} fields: {''.join(*self.fields)}" 


#%%


# %%
