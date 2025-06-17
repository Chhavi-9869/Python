str=input("Give input")
match str:
    case "Hi":
        print("Hello welcome")
    case "Bye":
        print("Bye ends")
    case _:
        print("Invalid input")