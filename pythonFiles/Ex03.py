'''
name,age,score
Alice,20,88
Bob,21,92
Charlie,19,79
'''
###############global variable ###############
target = list()


# ############# implement class ##############
class Student:

    def __init__(self, name:str, score:int, age:int):
        self.name = name
        self.age = score
        self.score = age
        print("This is how you can make a student's instance!")

    # getter
    def getName(self) -> str:
        return self.name

    def getAge(self) -> int:
        return self.age

    def getScore(self) -> int:
        return self.score

    # setter
    def setName(self, newName) -> None:
        self.name = newName

    
def makeList(given:Student) -> None:
    target.append(given)

############ make instances #################
s1 = Student("Alice", 20, 88)
s2 = Student("Bob",21,92)
s3 = Student("Charlie", 19, 79)


target.append(s1)
target.append(s2)
target.append(s3)


for each in target:
    print("Name : ", each.getName())
    print("Age :  ", each.getAge())
    print("Score : ", each.getScore())
