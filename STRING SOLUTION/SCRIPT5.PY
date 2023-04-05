def symmetric(a):
    b=(len(a)//2)
    c=a[:b]
    d=a[b:]
    if c==d:
        print(f"string {a} is symmetric !")
    else:
        print(f"string {a} is not symmetric")

def input1():
    e=input("Enter a string:")
    symmetric(e)

input1()
