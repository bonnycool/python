class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(f"the parent name:{self.name}")
        print(f"the parent age :{self.age}")

class student(person):
    def __init__(self,name,age,branch,sem):
        super().__init__(name,age)
        self.branch=branch
        self.sem=sem
    def stu_display(self):
        self.display()
        print(self.branch)
        print(self.sem)

s1=student("bonny",20,"csa",6)

s1.stu_display()
