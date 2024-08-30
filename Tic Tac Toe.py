# Abandoned and likely that I won't come back to it. Nonfunctional.




import random

turn = False
spots = ["   ","   ","   ","   ","   ","   ","   ","   ","   "]
corners = 0
botmove = 0
randombsgo = 0
dp1 = False
dp2 = False
dp3 = False
dp4 = False

def checkend():
    pass
    
def playerturn():
    print(spots)
    playermove = int(input("Select a square to mark with an X. Use single digit, non-zero numbers only."))
    playermove = playermove - 1
    if playermove < 9 and playermove > -1:
        if spots[playermove] == "   ":
            spots[playermove] = " X "
            botturn()
            pass
    else:
        print("Return a single digit, non-zero number that goes to an unoccupied place on the board please.")
        playerturn()

def botturn():
    global dp1, dp2, dp3, dp4
    global spots
    global corners
    
    if corners == 2: # Identify the endgame. It got you right where it wants you
        if spots[0] == " O " and spots[6] == " O ":
            if spots[8] == "   ":
                spots[8] = " O "
                dp1 = True
                playerturn()
                pass
            elif spots[2] == "   ":
                spots[2] = " O "
                dp2 = True
                playerturn()
            else:
                pass
        if spots[8] == " O " and spots[2] == " O ":
            if spots[0] == "   ":
                spots[0] = " O "
                dp3 = True
                playerturn()
            elif spots[6] == "   ":
                spots[6] = " O "
                dp4 = True
                playerturn()
            else: 
                pass
        else:
            pass

    if dp1 == True: 
        if spots[7] == "   ":
            spots[7] = " O "
            checkend()
            playerturn()
    elif spots[3] == "   ":
            spots[3] = " O "
            checkend()
            playerturn()
    if dp2 == True:
        if spots[1] == "   ":
            spots[1] = " O "
            checkend()
            playerturn()
    elif spots[3] == "   ":
            spots[3] = " O "
            checkend()
            playerturn()
    if dp3 == True:
        if spots[1] == "   ":
            spots[1] = " O "
            checkend()
            playerturn()
    elif spots[5] == "   ":
            spots[5] = " O "
            checkend()
            playerturn()
    if dp4 == True:
        if spots[7] == "   ":
            spots[7] = " O "
            checkend()
            playerturn()
    elif spots[5] == "   ":
            spots[5] = " O "
            checkend()
            playerturn()
      
    if (spots[3] == " X " and spots[5] == " X ") or (spots[1] == " X " and spots[7] == " X "): #Emergency block if they're gonna win by avoiding the corners
        if spots[4] == "   ":
            spots[4] = " O "
            print("DEBUG: MIDBLOCKED")
            playerturn()
        else:
            pass

    if spots[1] == " X " and spots[4] == " X ": #Emergency block if they're gonna win by rushing the middle (vertical)
        if spots[4] == "   ":
            spots[4] = " O "
            playerturn()
        else:
            pass
    if spots[3] == " X " and spots[5] == " X ": #Emergency block if they're gonna win by rushing the middle (horizontal)
        if spots[4] == "   ":
            spots[4] = " O "
            playerturn()
        else:
            pass

    if spots[0] == "   ": 
        spots[0] = " O "
        playerturn()
        pass
    elif spots[2] == "   ":
        spots[2] = " O "
        playerturn()
        pass
    elif spots[8] == "   ":
        spots[8] = " O "
        playerturn()
        pass
    elif spots[6] == "   " and corners < 2:
        spots[6] = " O "
        playerturn()
        pass
    elif spots[2] == "   " and corners < 2:
        spots[2] = " O "
        playerturn()
        pass
    else:
        pass
       

    randombsgo = random.randint(0, 8) 
    if spots[randombsgo] == "   ":
        spots[randombsgo] = " O "
        print("DEBUG: Random move made")
    playerturn()

if input("Will you go first or second? Return a 1 or a 2.") == ("1"): 
    spots[0] = " O "
else:
    playerturn()