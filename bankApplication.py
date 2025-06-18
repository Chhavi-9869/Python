import sys
list1=[]
def withdraw(bal,balance):
    balance-=bal
    return balance
def debit(bal,balance):
    balance+=bal
    return balance
balance=50000
x=balance
while(True):
    choice=int(input('''
                 1.Debit Money
                 2.Withdraw Money
                 3.Check balance
                 4.Passbook Printing
                 5.Exit'''))
    match(choice):
        case 1:
            balance=x
            bal=int(input("Enter amount to be debited"))
            x=debit(bal,balance)
            print("Final Balance:",x)
            list1.append("Debited amount:"+str(x))
        case 2:
            balance=x
            bal=int(input("Enter amount to be withdrawn"))
            if(bal>balance):
                print("Withdraw not possible")
            else:
                x=withdraw(bal,balance)
            print("Final Balance",x)
            list1.append("Withdrawn amount"+str(x))
        case 3:
            balance=x
            print("Total amount in bank:",balance)
        case 4:print(list1)

        case 5:sys.exit(0)
        case _:print("Invalid input")

print("------_______------")