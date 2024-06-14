import random

#print("Please select a value from 1 to 3")
computerChoice = random.randint(1,3)
userChoice = int(input("Please select a value from 1 to 3"))  
if userChoice > 3: 
    print("Please select a number that fits the criteria")  
    
userSign = ""
if userChoice == 1: 
    userSign = "Rock" 
elif userChoice == 2: 
    userSign = "Scissors"
elif userChoice == 3: 
    userSign = "Paper" 

computerSign = "" 
if computerChoice == 1: 
    computerSign = "Rock" 
elif computerChoice == 2: 
    computerSign = "Scissors" 
elif computerChoice == 3:
    computerSign = "Paper" 
print(f"You chose {userSign}") 
print(f"Computer chose {computerSign}") 
if userChoice == computerChoice: 
    print("It's a tie!") 
elif (userChoice == 1 and computerChoice == 3) or (userChoice == 2 and computerChoice == 1) or (userChoice == 3 and computerChoice == 2): 
    print('You lose') 
#elif (userChoice == 1 and computerChoice = 2) or (userChoice = 2 and computerChoice = 3) or (userChoice = 3 and computerChoice = 1): 
else:
    print('You win')  








  #  userLives = 3  
#uul = ('Current Lives =  ',userLives)
#umc = (input("You approach a cave, do you turn left or right? ")).lower()
#if umc == "left": 
   # print("good choice") 
  #  lakeDecision = input("You approach a lake, do you care to go for a swim? ").lower() 
  #  if lakeDecision == "no": 
  #      print("who knows what couldve been in that water") 
  #  elif lakeDecision == "yes": 
  #     orbDecision = input("you see a glowing orb on the bed of the water, do you try and take it? ").lower() 
  #     if orbDecision == "no": 
   #        print("Its probably a better idea not to touch it") 
  #     elif orbDecision == "yes": 
   #        print("as soon as you try and touch the orb, it disappears, who knows maybe the orb could show up later")
               
    

