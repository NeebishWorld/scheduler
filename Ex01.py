'''
1. csv file 
2. dictionary
3. class
'''
import csv

####################### global variable #########################
students = list()



################## implement functions ###########################
def readCSVFile(givenFile) -> list:
    result = list()
    with open(givenFile, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        
        for each in reader:
            result.append(each)

    return result


def allNames(given: list) -> None:
    '''
    This function prints out all names in the given student list
    '''
    for eachName in given:
        print(eachName[0])

def allAges(given : list) -> None:
    '''
    This fucntion prints out all ages in the given student list
    '''
    for each in given:
        print(each[1])


################# call the functions #############################
print(readCSVFile("./here.csv"))

# allNames(students)
# allAges(students)