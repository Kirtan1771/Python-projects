'''
1 for rock
-1 for paper
0 for scissors
'''

import random

computer = random.choice([1, -1, 0])
you = input("Enter your choice: ")
youDict = {"rock": 1 , "paper": -1 , "scissors": 0}
reverseDict = {1:"rock" , -1:"paper" , 0:"scissors"}
yourNum = youDict[you]

print(f"You choose {reverseDict[yourNum]}\nComputer choose {reverseDict[computer]}")

if(computer == yourNum):
    print("Draw!")

else:
    if(computer == -1 and yourNum == 1):
        print("You loose!")

    elif(computer == -1 and yourNum == 0):
        print("You Win!")
    
    elif(computer == 1 and yourNum == 0):
        print("You loose!")
        
    elif(computer == 1 and yourNum == -1):
        print("You Win!")
        
    elif(computer == 0 and yourNum == -1):
        print("You Loose!")
        
    elif(computer == 0 and yourNum == 1):
        print("You Win!")

    else:
        print("Something went wrong")
   
