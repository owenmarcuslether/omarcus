# Tic Tac Toe 
turn = False
aa = "   "
ab = "   "
ac = "   "
ba = "   "
bb = "   "
bc = "   "
ca = "   "
cb = "   "
cc = "   "
spots = [aa,ab,ac,ba,bb,bc,ca,cb,cc]
corners = 0
botmove = 0

def playerturn():
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
    if ba == " X " and bc == " X " or ab == " X " and cb == " X ": #Emergency block off if they're gonna win by avoiding the corners
        if bb != " O " or bb != " X ":
            bb = " O "
        else:
            pass


    if aa == "   ":
        aa = " O "
        playerturn()
    elif ac == "   ":
        ac = " O "
        playerturn()
    elif ca == "   ":
        ca = " O "
        playerturn()
    elif cc == "   " and corners <3:
        cc = " O "
        playerturn()
       
    if corners == 3:
        pass
    print(spots)
    playerturn()

if input("Will you go first or second? Return a 1 or a 2.") == ("1"):
    playerturn()
else:
    botturn()