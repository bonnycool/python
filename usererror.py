

class error(Exception):
    def __init__(self,alert):
        self.alert=alert

def validate(age):
    if age<18:
        raise error("invalid age")


try:
    age=int(input())
    validate(age)
    print(age)
except error as e:
    print(e)

except ValueError:
    print("enteer a number")    
