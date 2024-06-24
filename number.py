with open("num.txt","r") as f:
    numbers=f.read()

num=numbers.strip().split()
even=[]
odd=[]
for each in num:
    each=int(each)
    if each%2==0:
        
        even.append(str(each))
    else:
        str(each)
        odd.append(str(each))


    
even_content = "\n".join(even)
odd_content = "\n".join(odd)   
print(even_content)
with open("even.txt","w") as e:
    e.write(even_content)

with open("odd.txt","w") as o:
    o.write(odd_content)

