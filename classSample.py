class Worker:
    # 생 성 자  / constructor 
    def __init__(self, firstName, lastName, birth, contact="01024447777", days=0, hours=0, salary=0):
        self.firstName = firstName # str
        self.lastName = lastName # str
        self.birth = birth # str ex)"1999.10.30"
        self.contact = contact # str ex) "01024631234"
        self.workingDays = days # int
        self.workingHrs = hours # float
        self.salary = salary    # float

    # getter
    def getFirstName(self) -> str:
        '''
        return the first name
        '''
        return self.firstName

    def getLastName(self) -> str:
        '''
        return the last name 
        '''
        return self.lastName

    def getBirth(self) -> str:
        return self.birth

    def getBirthYear(self)->int:
        '''
        Return the birth year as int
        '''
        temp = self.birth

        storage = list()
        word = ""
        for each in temp:
            if each != '.':
                word = word + each
            else:
                storage.append(word)
                word = ""
        storage.append(word)

        # print(storage)    

        newStorage = list()
        for each in storage:
            newStorage.append(int(each))
        
        # print(newStorage)

        return newStorage[0]

    def getBirthYear02(self)->int:
        return int(self.birth.split(".")[0])

    def getContact(self) -> str:
        return self.contact

    def getWorkingDays(self) -> int:
        return self.workingDays

    def getWorkingHours(self) -> float:
        return self.workingHrs

    def getSalary(self) -> float:
        return self.salary

    # setter
    def setFirstName(self, newFristName:str) -> None:
        '''
        replace the first name with the new name
        '''
        self.firstName = newFristName

    def setLastName(self, newLastName:str) -> None:
        self.lastName = lastName

    def setBirth(self, birth:str) -> None:
        self.birth = birth

    def setContact(self, newContact:str) -> None:
        self.contact = newContact

    def setWorkingDays(self, newWorkingDays:int) -> None:
        self.days = newWorkingDays

    def setWorkingHours(self, newWorkingHours:float) -> None:
        self.workingHrs = newWorkingHours
        
    def setSalary(self, newSalary:float) -> None:
        self.salary = newSalary



class Teacher(Worker):
    def __init__(self, subjects:list, email:str, firstName, lastName, birth, contact="01024447777", days=0, hours=0, salary=0):
        super().__init__(firstName, lastName, birth, contact, days, hours, salary)
        self.subjects = subjects
        self.email = email

    # setter
    def setSubjects(self, subjectLists:list)->None:
        self.subjects = subjectLists

    def setEmail(self, newEmail:str)->None:
        self.email = newEmail

    # getter 
    def getSubject(self) -> list:
        return self.subjects

    def getEmail(self) -> str:
        return self.email



t01 = Teacher(["CS", "CalBC"], "adam.oh@libertas-jesus.org", "Adam", "Oh", "1999.7.25", "0102463XXXX", 5, 7, 100000)
print(t01.getBirth())
print(t01.getBirthYear())
print(t01.getBirthYear02())