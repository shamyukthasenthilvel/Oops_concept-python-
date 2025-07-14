class Student:
    def __init__(self,name,mark):
        self.Name=name
        self.Mark=mark
    def __str__(self):
        name = f"student name : {self.Name}"
        mark = f"student mark : {self.Mark}"
        return f"{name}\n{mark}"


s1=Student("shamy",65)
s2=Student("abi",86)
s3=Student("anu",93)
s4=Student("ad",49)
s5=Student("palani",76)

print(s1)
print(s2)
print(s3)
print(s4)
print(s5)


