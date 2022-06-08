attempts = 0


# asking the user the number of attempts they want
def num_of_attempts(attempts):
    while True:
        try:
            num = int(input("How many number of attempts from 1-10 do you want?"))
            if 0 < num < 11:
                print("You have {} attempts".format(num))
            else:
                print("Please choose a number between 1-10")
        except ValueError:
            print("Please choose a number")
            continue


# asking the user if they want to do attempts
yes_no = num_attempts = input("Do you wish to add number of attempts?")
if num_attempts == "yes" or "y":
    num_of_attempts(attempts)

