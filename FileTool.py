#%%
from pathlib import Path
import os
#TODO pandas will load into python environment if it is necessary
import pandas
import sys
class FileTool:
    

    def __init__(self, path = None, *args) -> None:
        self.userChoice()
        self.path = path
        self.fields = args
        

    def append(self, *args):
        """ The append function stands for appending the values at the end of the csv file which is specified"""
        pass

    # the main idea of being property that method is can be used like a variable
    @property
    def isFileExists(self):
        """ This checks the entered file exists or not"""
        if self.path.find('/') == -1: # if the given path is the data's itself
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
                flag = False
                pass
            elif user_input == '2':
                flag = False
                pass
            elif user_input == '3':
                flag = False
                pass
            elif user_input == '4':
                flag = False
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
    
    def isFeaturesMatches(self):
        """ Checks the featrues matches or not"""
        pass

    def exportToJson(self):
        """ export the one line of data to JSON file"""
        pass

    def __repr__(self) -> str:
        return f"folder:{self.path.split('/')[:-1]} file:{self.path.split('/')[-1]} fields: {''.join(*self.path)}" 


#%%

# Test

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
        flag = False
        pass
    elif user_input == '2':
        flag = False
        pass
    elif user_input == '3':
        flag = False
        pass
    elif user_input == '4':
        flag = False
        pass
    elif user_input == '0':
        print("Bye bye")
        sys.exit(0)
    else:
        try:
            if int(user_input) not in range(0,5):
                print("Please enter a number range in between 0 and 4")
        except:
            print("Wrong character please a number range in between 0 and 4")
# %%
