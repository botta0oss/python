import random

''' 
simple Rock Paper Scissor game 
(coded along with "Tech with Tim - 5 Mini Python Projects - For Beginners" https://www.youtube.com/watch?v=DLn3jOsNRVE)
then added by myself some variations like scoreboard and exit messages 
'''




# variables storing wins from player and computer
user_wins = 0
computer_wins = 0

# initializing a list used later to check and validate the user input
options = ["rock", "paper", "scissor"]

# starting the loop that keep the game alive or quit the program if 
# q is casted
while True:
    print(''' ------------| Rock Paper Scissor |--------------- \n Rules:\n 
    \t-Type rock/paper/scissor to play\n \t-Type q to quit the game\n \t-Type score to wiew the scoreboard''')
    user_input = input("< ").lower()
    if user_input == "q":
        break
    
    # creating a little scoreboard to be wiewed during gam when requested
    if user_input == "score":
        print(" ------------| Scoreboard |--------------- \n| player: ", user_wins, "\n| computer: ", computer_wins )

    # check multiple thing in one line using a list
    # 'not' reverse the if check
    if user_input not in options:
        continue

     
    # variable with a random number generated between 0 and 2 (0 1 2)
    # going to be used in the computer choice
    random_number = random.randint(0, 2)

    # rock: 0 , paper: 1 , scissor: 2
    # use the list previously created (options) to match the
    # the random number chosen with the index of the item in the list
    computer_pick = options[random_number]
    print("Computer picked ", str(computer_pick) + "." )

    # creating the player condition to win 
    # only three condition cause if they aren't true player lost
    if user_input == "rock" and computer_pick == "scissor":
        print("you won!")
        user_wins += 1
        

    elif user_input == "paper" and computer_pick == "rock":
        print("you won!")
        user_wins += 1
        

    elif user_input == "scissor" and computer_pick == "paper":
        print("you won!")
        user_wins += 1
    
    elif user_input == computer_pick:
        print("it's a draw")
        
    else: 
        print("you lost!")
        computer_wins +=1


# diffrent message cases when exiting the game (with a little bit of spice...)

if user_wins == 0 and computer_wins == 0:
    print("scared of loosing...")

elif user_wins > computer_wins and computer_wins != 0:
    print("you won, that's what u are supposed to do don't you dare exult ")

elif user_wins == computer_wins and user_wins != 0:
    print("it's a draw, at least you don't suck")
    
else:
    print("the computer won, you really suck... ")







