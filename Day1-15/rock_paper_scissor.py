import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
user_choice = int(input("Enter 0 for rock,1 for paper, or 2 for scissors: \n"))

if user_choice ==0:
    print(rock)
elif user_choice ==1:
    print(paper)
else:
    print(scissors)

computer_choice =random.randint(0,2)

if computer_choice ==0:
    print(rock)
elif computer_choice ==1:
    print(paper)
else:
    print(scissors)



if user_choice == computer_choice:
    print("It's a tie")
elif user_choice == 0 & computer_choice ==2:
    print("you win")
elif user_choice == 1 & computer_choice ==0:
    print("you win")
elif user_choice == 2 & computer_choice ==1:
    print("you win")
else:
    print("You lose")