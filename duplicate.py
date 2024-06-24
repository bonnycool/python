with open("bonny.txt","r") as f:
    content=f.read()
word=content.split()
unique=set(word)

print(unique)    

with open("new.txt","w") as q:
    for word in unique:
        q.write(word +"\n")\
        