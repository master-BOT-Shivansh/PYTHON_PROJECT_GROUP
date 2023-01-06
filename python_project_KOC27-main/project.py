import math
def add(a,b):
    print("ans",a+b)
def subtract(a,b):
    print("ans",a-b)
def multiply(a,b):
    print("ans",a*b)
def divide(a,b):
    print("ans",a/b)
def reminder(a,b):
    print("ans",a%b)
def exponent(a,b):
    x=1
    for i in range (0,b):
        x=x*a
    print("ans",x)

print("single number operation like sqroot,conversion etc (select 1) or duble number operation like(+-*/) (select 2) \nTYPE 1 OR 2" )

op=int(input("YOUR SELECTED :"))
if op==1:
    print("what operation you want to perform\nTYPE\nsqroot for square root\nsin for sine\ncos for cosine\ntan for tangent\ndTr for degree to radian\nrTd for radian to degree")
    operation=input()
    number=int(input("give the number:"))
    if operation=="sqroot":
        print("ans",math.sqrt(number))
    elif operation=="sin":
        print("ans",math.sin(number))
    elif operation=="cos":
        print("ans",math.cos(number))
    elif operation=="tan":
        print("ans",math.tan(number))
    elif operation=="rTd":
        print("ans",math.degrees(number))
    elif operation=="dTr":
        print("ans",math.radians(number))
    else:
        print("ERROR!!!,objects are case sensitive try AGAIN")
elif op==2:
    print("what operation you want to perform\nTYPE\nadd for addition\nsub for subtraction\nstar for multiplication\ndiv for divsion\npower for exponent\nmod for remainder")
    operation=input()
    x=int(input("give the number1:"))
    y=int(input("give the number2:"))
    if operation=="add":
        add(x,y)
    elif operation=="sub":
        subtract(x,y)
    elif operation=="div":
        divide(x,y)
    elif operation=="star":
        multiply(x,y)
    elif operation=="power":
        exponent(x,y)
    elif operation=="mod":
        reminder(x,y)
    else:
        print("ERROR!!!,objects are case sensitive try AGAIN")
