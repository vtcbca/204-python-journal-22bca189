def paliwordcount(a):
    b=a.split(" ")
    c=0
    d=[]
    for i in b:
        if (i==i[::-1]):
            c=c+1
            d.append(i)
    if c>0:
        print(" Palindrome Word In Sentence Is {c} And Palindrome Words Are:{d}.")              
    else:
        print(" No Palindrome Word in Sentence!!!")    
a=input("enter a sentece:")
paliwordcount(a)
