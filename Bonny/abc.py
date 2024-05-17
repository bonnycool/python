class Minor(Exception):
    pass

try:
    age=19
    def CanHit(age):
        if(age<18):
            raise(Minor("nigga whattt"))
        else:
            print("smash it")
    CanHit(age)
except Minor as error:
    print(error)