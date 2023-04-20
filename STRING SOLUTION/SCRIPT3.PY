def evenstr(b):
    c=[]
    count=0
    for i in b:
        if(len(i)%2==0):
            c.append(i)
            count=count+1
    if(count>0):
         print(f"the number of even string is {count} and string:{c}")

    else:
         print("no even string available!")
b=[]
for i in range(5):
     e=input(f"Enter string:{i+1}:")
     b.append(e)
evenstr(b)
 
