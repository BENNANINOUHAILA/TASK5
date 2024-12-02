print("<<Calculator>>")
print("1-sum \n")
print("2-minus \n")
print("3-divide \n")
print("4-power \n")
print("5-multi \n")
print("enter two numbers")
a=int(input("a="))
b=int(input("b="))
print("chose operation")
op=int(input("operation number : "))
def sum(a,b):
    return a+b
def minus(a,b):
    return a-b
def divide(a,b):
    return a/b
def power(a,b):
    return a**b
def multi(a,b):
    return a*b
if(op==1):
    print("sum=",sum(a,b))
elif(op==2):
    print("minus=",minus(a,b))
elif(op==3):
    if(b==0):
        while(b==0):
            print("enter a number>0")
            b=int(input())
        print("divide=",divide(a,b))
    else:
        print("divide=",divide(a,b))
elif(op==4):
    print("power=",power(a,b))
else:
    print("multiplication=",multi(a,b))

