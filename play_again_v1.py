print("What can you do to help reduce deforestation?")


print("------------------------------")
print("Thank you for playing the quiz")
print("------------------------------")

yes_no = replay = input("Do you wish to play the quiz again?")
if replay == "yes" or replay == "y":
    print("Welcome back to the quiz")
elif replay == "no" or replay == "n":
    print("You are exiting the quiz")
    exit(0)
