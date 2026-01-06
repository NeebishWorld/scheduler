class Worker:
    # 생 성 자  / constructor 
    def __init__(self, firstName, lastName, birth, contact="01024447777", days=0, hours=0, salary=0):
        self.firstName = firstName # str
        self.lastName = lastName # str
        self.birth = birth # str ex)"1999.10.30"
        self.contact = contact # str ex) "01024631234"
        self.workingDays = days # int
        self.workingHr = hours # float
        self.salary = salary    # float

    # getter
        def getFirstName(self) -> str:
            return self.firstName

    # setter
        def setFirstName(self, newFristName) -> None:
            self.firstName = newFristName





# Make a class instance
Worker("Adam", "Oh", "1989.10.25")
Worker("Seoneun", "Oh", "1993.07.01")


    