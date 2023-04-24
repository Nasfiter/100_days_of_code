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


import random
simbols_list = [rock, paper, scissors]

your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scessors: "))
computer_choice = random.randint(0, 2)
winner_or_not = ["Won!", "Lose :(", "Drow"]
winer_result = 2 # in case is computer and your choice are ==. the logic will skip if statejent and will go to result as drow

if your_choice != computer_choice:  
    if your_choice == 0 and computer_choice != 1:
        winer_result = 0
    elif your_choice == 1 and computer_choice != 2:
        winer_result = 0
    elif your_choice == 2 and computer_choice != 0:
        winer_result = 0
    else:
        winer_result = 1
    
       
if your_choice > 2 or your_choice < 0:
    print("Invalid number")
else:
    print(simbols_list[your_choice])
    print(f"Computer chose:\n{simbols_list[computer_choice]}")
    print(winner_or_not[winer_result])
