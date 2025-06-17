import random
attempt=int(input("Enter number of attempts"))
a=random.randint(1,100)
i=1
while(i<=attempt):
    print("Attempt:",i)
    b=int(input("Guess a number"))
    if(b>a):
        print("Your number is too big")
    elif(a>b):
        print("Your number is too small")
    else:
        print("Correct guess")
        break
    i+=1
print("Game over")


    
  