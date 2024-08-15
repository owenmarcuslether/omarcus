# Tic Tac Toe 
import random
nevermoved = False
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
tlcorner = 1
trcorner = 1
blcorner = 1
brcorner = 1
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
#    if nevermoved == True:
#        spots[0] = " O "
#    if aa == " X ":
#        tlcorner = 0
#    if ac == " X ":
#        trcorner = 0
#    if ca == " X ":
#        blcorner = 0
#    if cc == " X ":
#       brcorner = 0
#    if tlcorner == 1 and trcorner == 1 and blcorner == 1 and brcorner == 1:
#        pass
    botmove = random.randint(-1,9)
    if spots[botmove] == " X ":
        botmove = random.randint(-1,9)
    else: 
        spots[botmove] = " O "
    print(spots)
    playerturn()

if input("Will you go first or second? Return a 1 or a 2.") == ("1"):
    playerturn()
else:
    nevermoved = True
    botturn()