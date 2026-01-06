import csv 
from datetime import date
'''
1. read info from the csv file
2. create class instances with those info
'''


class Person:
    def __init__(self, firstName:str, lastName:str, age:int):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
    

class Instructor(Person):
    def __init__(self, firstName:str, lastName:str, age:int, subjects:list, notAvail:str):
        super().__init__(firstName, lastName, age)
        self.subjects = subjects
        self.notAvail = notAvail


class Scheduler:

    def __init__(self):
        self.instructors = list()

    def readCSV(self) -> None: 
        '''
        Read the info csv file and make class instances with those data properly.
        All instacnes will be stored in the list, instructors.
        '''
        with open('./info.csv', mode='r', encoding='utf-8') as file:
            csvFile = csv.reader(file, delimiter=',')
            header = next(csvFile) # Stores the first row (header)
            # print(f"Skipped Header: {header}")
            for each in csvFile:
                self.instructors.append(Instructor(each[1], each[0], date.today().year - int(each[2].split('-')[0]), each[3].split('|'), each[4]))

    
    def display(self) -> None:
        '''
        Display all instructors' names
        '''
        for each in self.instructors:
            print("Full Name : ", each.firstName, " ", each.lastName)
            print("Age : ", each.age)
            print("Teaching Subjects : ")
            for eachSubject in range(0, len(each.subjects)):
                print("\t" + str(eachSubject+1) + "  ", each.subjects[eachSubject])
            print("Availability : ", each.notAvail)
            print("\n####################################################################\n")
    






if __name__ == "__main__":
    s = Scheduler()
    s.readCSV()
    s.display()


