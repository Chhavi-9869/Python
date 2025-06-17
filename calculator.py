import sys
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

while(True):
    choice=int(input('''Enter your choice:
          1.Addition
          2.Subtraction
          3.Multiplication
          4.Division
          5.Exit\n '''))
    
    if(choice!=5):
       a=int(input("Enter first number:"))
       b=int(input("Enter second number"))
    match choice:
        case 1:
            x=add(a,b)
            print("Addition:",x)
        case 2:
            x=sub(a,b)
            print("Subtraction:",x)
        case 3:
            x=mul(a,b)
            print("Multiplication:",x)
        case 4:
            x=div(a,b)
            print("Division:",x)
        case 5:sys.exit(0)

    
    