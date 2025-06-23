class Person:
    def getGender(self):
        pass
class Male(Person):
    def getGender(self):
        print("Male")
class Female(Person):
    def getGender(self):
        print("Female")
m = Male()
f = Female()
m.getGender()
f.getGender()
