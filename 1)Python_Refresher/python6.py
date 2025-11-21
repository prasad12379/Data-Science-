#file handeling
file=open("a.txt","r") #r means read mode
a=file.read()
file.close()
print(a)

#OR new method

with open("a.txt","r") as file2:
    b=file2.read() #no need to close file
    print(b)
    
with open("a.txt","w") as file3:
    s=" my name is pd"
    file3.write(s)
    