# import the time module
import time


# define the countdown func.
def the_countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        time_sec -= 1

    print('Fire in the hole!!')

    # function call
    the_countdown(int(time_sec))


# asking the user if they wanna input countdown
user_time = input("Do you wish to add a countdown?")
if user_time == "yes" or "y":
    time_sec = input("Please enter the time in seconds: ")
