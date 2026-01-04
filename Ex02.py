'''
name,age,score
Alice,20,88
Bob,21,92
Charlie,19,79

We are goint to make a data structure with these data
'''

d = dict()
s1 = {"name" : "Alice", "age" : 20, "score" : 88}
s2 = {"name" : "Bob", "age" : 21, "score" : 92}
s3 = {"name" : "Charlie", "age" : 19, "score" : 79}

result = list()
result = [s1, s2, s3]

print(result)

####################### global variable #####################
target = list()



######################### implement functions ###############
def makeDict01(name:str, age:int, score:int) -> None:
    target.append({"name" : name, "age": age, "score": score})

def makeDict02(name:str, age:int, score:int) -> None:
    result = dict()
    result["name"] = name
    result["age"] = age
    result["score"] = score

    target.append(result)


def allNames(given: list) -> None:
    for each in given:
        print(each['name'])

def allAges(given: list) -> None:
    for se in given:
        print(se["age"])

######################### call functions ####################

makeDict01("Alice", 20, 88)
makeDict02("Bob", 21, 92)
makeDict01("Chalie",19,79)

allNames(target)
allAges(target)