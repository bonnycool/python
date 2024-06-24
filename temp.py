file_name='bonny.txt'
file_content="""hello world!
this is a new file
created by bonny
for testing the program"""

with open("bonny.txt","w") as f:
    f.write(file_content)

with open("bonny.txt","r") as file:
    lines=file.readlines()

print(lines)
largest_word=''
for line in lines:
    print(line.strip())
    words=line.strip().split()
    for word in words:
     if len(word)>len(largest_word):
        largest_word=word

print(largest_word)

cleaned=[line.strip() for line in lines]
print(cleaned)   

