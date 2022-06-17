name_user = input("Hello user, this is a little quiz about deforestation what is your name?")
print("Hello {}".format(name_user).title())


# asking the user question
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            response = "Yes"
            return response

        elif response == "no" or response == "n":
            response = "No"
            return response
        else:
            print("Please answer yes/no")


# if user doesn't know what deforestation is
def facts_about_deforestation():
    print("What is deforestation?")
    print()
    print("Deforestation is the removal of a forest or stand of trees from land that is then"
          "converted to non-forest use like buildings, etc.")


# how to play the game
def how_to_play():
    print("This is a small quiz game where you need to answer the question about deforestation")
    print()
    print("The rules:")
    print("There are 6 question you need to answer")
    print("Answer the question by using the answers listed below")
    print("There will be some words that ")


# asking the user if they know about deforestation
user_question = yes_no("Do you know about deforestation {}?".format(name_user).title())
if user_question == 'no' or user_question == 'n':
    facts_about_deforestation()

print("The quiz continues")

how_to_play()
