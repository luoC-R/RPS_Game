# Check that users have entered a valid
# option based on a list
def string_checker(question, valid_ans=("yes", "no")):

   error = f"Please enter s valid option from the following list: {valid_ans}"

   while True:

       # Get user response and make sure it's lowercase
       user_response = input(question).lower()

       for item in valid_ans:
           # check if the user response is a word in the list
           if item == user_response:
               return item

           # check if the user response is the same as
           # the first letter of an item in the list
           elif user_response == item[0]:
               return item

       # print error if user does not enter something that is valid
       print(error)
       print()


# Displays instructions
def instruction():
    print('''

**** Instructions ****
 
To begin, choose the number of rounds (or press <enter> for
infinite mode).

The play against the computer.   You need to choose R (rock),
P (paper) or S (scissors).

The rules are as follows:
o   Paper beats rock
o   Rock beats scissors
o   Scissors beats paper

Press <xxx> to end the game at anytime

Good Luck
    ''')


# Main routine
print()
print("💎📄✂ Rock / Paper / Scissors Game ✂📄️💎")
print()

# ask user if they wang to see the instructions and display
# them if requested
want_instructions =string_checker("Do you want to see instructions? ")

# checks users enter yes (y) or nno (no)
if want_instructions == "yes":
    instruction()

    print("program continues")
















