import random #To generate random number
while True:
    n=random.randint(0,100)
    i = 7
    g = 0
    print("\t\t\t\t ##### welcome to game of guessing the number #####\n")
    print("Rules are as follows:")
    print("1)You have 7 chances.\n2)The number is between 1 to 100.\nLet's Start \n")
    while i >= 1:
        a = int(input("\nWhich number comes in your mind : "))
        i = i - 1
        g = g + 1
        if a > n:
            print(f"\nThe number is less than {a}. Try again. You have {i} chances left.. ")
            if i == 0:
                print("\n\t\t\tWrong Guess!!!. All chances are over.")
                break
            else:
                continue
        elif a == n:
            print("\nCongratulations 🤩🤩 !! You have guessed the number correctly")
            print(f"You took {g} chances Guess the number..")
            break

        else:
            print(f"The number is greater than {a}. Try again. You have {i} chances left.. ")
            if i == 0:
                print("\n\t\t\tWrong Guess!!!. All chances are over.")
                break
            else:
                continue

    b = input("\n\t Do You wish to try game once again (y/n): ")
    if b == "n":
        print("\n\tThanks for playing this game!!!")
        break
    else:
        continue
