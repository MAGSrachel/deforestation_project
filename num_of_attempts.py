
# asking the user the number of attempts they want
def num_of_attempts(attempts):
    while True:
        try:
            num = int(input("How many number of attempts from 1-10 do you want?"))
            if 0 < num < 11:
                print("You have {} attempts".format(num))
                num += attempts
                break
            else:
                print("Please choose a number between 1-10")
        except ValueError:
            print("Please choose a number")
            continue


# asking the user if they want to do attempts
yes_no = num_attempts = input("Do you wish to add number of attempts?")
if num_attempts == "y" or num_attempts == "yes":
    attempts = 0
    num_of_attempts(attempts)
elif num_attempts == "n" or num_attempts == "no":
    print("Continue")


def run_out(attempts):
    if attempts > 0:
        print("You have run out of attempts")
        exit(0)
    else:
        print("Continue")
