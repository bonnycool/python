class error(Exception):
    def __init__(self,mess):
        self.mess=mess

def validate(age):
    if age<0 or age>150:
        raise  error("Invalid age")

try:
    age=int(input())
    validate(age)
    print(age)

except error as e:
    print("yo aare too oold for thatr ")

except ValueError:
    print("please enter a valid number")