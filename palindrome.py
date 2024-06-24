def is_palindrome(word):
    word=word.lower()

    return word==word[::-1]

palin=[]

with open("bonny.txt","r") as f:
    lines=f.readlines()
print(lines)    

for word in lines:
    words=word.split()
   
    for each in words:
        if is_palindrome(each):
            palin.append(each)

print(palin)