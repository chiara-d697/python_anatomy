import random

def rps(user, computer):
    if user == computer:
        return 'Draw!'
    elif (user == 'Scissors' and computer == 'Rock') or (user == 'Paper' and computer == 'Scissors') or (user == 'Rock' and computer == 'Paper') :
        return 'Computer wins!'
    else :
        return 'You win, queen!'

user_choice = str(input("Please select R, P or S:"))
if user_choice == "R":
    user_choice_1 ="Rock"
elif user_choice == "P":
    user_choice_1="Paper"
else:
    user_choice_1 = "Scissors"
print("You have chosen", user_choice_1)

computer_choice = random.randint(0,2)

if computer_choice == 0:
    computer_choice_1 ="Rock"
elif computer_choice == 1:
    computer_choice_1="Paper"
else:
    computer_choice_1 = "Scissors"
print("Your rival has chosen", computer_choice_1)

result = rps(user_choice_1, computer_choice_1)
print(result)