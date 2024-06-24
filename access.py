class student:
    def __init__(self,name,branch):
        self.name=name
        self.branch=branch
    
    def get_name(self):
        return self.name
    def get_branch(self):
        return self.branch
    
    def set_name(self,name):
        self.name=name
    def set_branch(self,branch):
        self.branch=branch 

    def display(self):
        print(f"name:{self.get_name()}")
        print(f"branch:{self.get_branch()}") 



s1=student("bonny","csa")
s1.display()
s1.set_name("basil")
s1.set_branch("mech")
print()
s1.display()

