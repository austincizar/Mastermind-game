#Rules of the game
# Two players play the game against each other; let’s assume Player 1 and Player 2(PC).

# An example(Either PC or player 1 can start first):
# Player 1 plays first by setting a multi-digit number.
# Player 2 now tries his first attempt at guessing the number.
# If Player 2 succeeds in his first attempt (despite odds which are highly unlikely) he wins the game and is crowned Mastermind! If not, then Player 1 hints by revealing which digits or numbers Player 2 got correct.
# The game continues till Player 2 eventually is able to guess the number entirely.
# Now, Player 2 gets to set the number and Player 1 plays the part of guessing the number.
# If Player 1 is able to guess the number within a lesser number of tries than Player 2 took, then Player 1 wins the game and is crowned Mastermind.
# If not, then Player 2 wins the game.


import random

rand_num = str(random.randrange(1000,9999))
rand_list = list(rand_num)
#print (rand_list)


# code for PC to pick the number while the Player guesses 
correct = ["X", "X", "X", "X"]        
def game():
    player = (input("Guess the hidden number: "))
    player_list = list(player)
    
    C1=-1
    for x in player_list:
        C1+=1
        
        if player_list[C1] == rand_list[C1]:
            
            correct[C1]=rand_list[C1]
            #print("This is correct: ", correct) #for debugging
      
    print (correct)
    
    c2 = -1
    for q in correct:
        c2 += 1
        if q == "X":
            print("Number ", c2+1, " is missing")
        
        if "X" not in correct:
            return ("You win")
    
def player_run():
    x=0
    while "X" in correct:
        x+=1
        G = game()
    if x == 0 and "X" not in correct:
        print ("You are the MASTERMIND!")
        return    
    return (x)
       
    


# code for player to pick the number while the computer guesses 

pc_correct = ["X", "X", "X", "X"]


def comp():

    comp_g = str(random.randrange(1000,9999))
    comp_guess = list(comp_g)
    c3 = -1
    
    for x in pc_correct:
        c3 += 1
        if x != "X":
            comp_guess[c3] = pc_correct[c3]
    c4 = -1
    for x in player_num:
        c4 += 1
        if comp_guess[c4] == player_num[c4]:
            pc_correct[c4] = player_num[c4]
    print (pc_correct)   
    
    
def pc_run():
    c5=0
    while "X" in pc_correct:
        c5+=1
        comp()
    if c5 == 0 and "X" not in pc_correct:
        print ("The computer is the MASTERMIND!")
        return
    
        
    return (c5)    


play=input("Input 1 for player to guess first and 2 for pc to guess first: ")
while play:
    if play == "1":
        player_count = player_run()
        print("")
        print("Now it is PC's turn to guess")
        print("")
        player_num  = input("Enter a number between 1000 and 9999: ")
        pc_count = pc_run()
        break
    elif play == "2":
        player_num  = input("Enter a number between 1000 and 9999: ")
        pc_count = pc_run()
        print("")
        print("Now it is your turn to guess")
        print("")
        player_count = player_run()
        break
    else:
        print ("Wrong input, try again!")
        play=input("Input 1 for player to guess first and 2 for pc to guess first: ")
 

if player_count < pc_count:
    print(player_count, "<", pc_count)
    print("You win! You are the MASTERMIND!")
elif player_count > pc_count:
    print(player_count, ">", pc_count)
    print("PC wins! The PC is the MASTERMIND!")
else:
    print("Its a tie.")