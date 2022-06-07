# asking the user question
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
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
    print("There are () question you need to answer")
    print("Answer the question by using the answers listed below")


# asking the user if they know about deforestation
user_question = yes_no("Do you know about deforestation?")
if user_question == 'no' or 'n':
    facts_about_deforestation()

print("The quiz continues")

how_to_play()
