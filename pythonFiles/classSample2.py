class Person:
    def __init__(self, name:str, birth:str, gender:str):
        self.name = name
        self.birth = birth
        self.gender = gender

class Instructor(Person):
    def __init__(self, name:str="", birth:str="", gender:str="", email:str="", subjects:list=[]):
        super().__init__(name, birth, gender)
        self.subjects = subjects
        self.email = email

    def setByUser(self):
        '''
        Let users type in their personal information
        '''
        print("This is where you can enter your personal information!")
        self.name = input("What is your name ? (first last) : ")
        self.birth = input("When did you born ? (1889.10.24) : ")
        self.gender = input("What is your gender ? (F or M) : ")
        self.email = input("What is your email ? : ")


if __name__ == '__main__': 
    teacher01 = Instructor()
    teacher01.setByUser()
    print(teacher01.name)