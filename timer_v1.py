import time

list_of_time = ["1 minute", "2 minute", "3 minutes", "4 minutes", "5 minutes"]


def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        time_sec -= 1

    print("stop")


time_user = input("Do you wish to do a challenge where you have a limited time to answer the question?")
if time_user == "yes" or "y":
    print(list_of_time)
    user = input("How many minutes do you want?")
    if user == "1":
        countdown(60)
    elif user == "2":
        countdown(120)
    elif user == "3":
        countdown(180)
    elif user == "4":
        countdown(240)
    elif user == "5":
        countdown(300)
    else:
        print("Please choose one of the options")
