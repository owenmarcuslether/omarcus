sp = " "
ro = "#"
ki = "K"
wa = "W"
rox = 0
roy = 0
aa = [0,0,sp]
ab = [1,0,sp]
ac = [2,0,sp]
ad = [3,0,sp]
ae = [4,0,sp]
ba = [0,1,sp]
bb = [1,1,sp]
bc = [2,1,sp]
bd = [3,1,sp]
be = [4,1,sp]
ca = [0,2,sp]
cb = [1,2,sp]
cc = [2,2,sp]
cd = [3,2,sp]
ce = [4,2,sp]
da = [0,3,sp]
db = [1,3,sp]
dc = [2,3,sp]
dd = [3,3,ki]
de = [4,3,sp]
ea = [0,4,wa]
eb = [1,4,sp]
ec = [2,4,sp]
ed = [3,4,sp]
ee = [4,4,sp]
boardapr = [sp,sp,sp,sp,sp]
boardbpr = [sp,sp,sp,sp,sp]
move = "no"
boarda = [aa,ab,ac,ad,ae]
boardb = [ba,bb,bc,bd,be]
boardc = [ca,cb,cc,cd,ce]
boardd = [da,db,dc,dd,de]
boarde = [ea,eb,ec,ed,ee]

print("You are robot. Find kitten.")
while sp == " ":
    if move == "please": print(rox, roy)
    elif move == ("a") or ("d") or ("s") or ("w"):
        if move == "a": rox = rox -1
        elif move == "d": rox = rox +1
        elif move == "s": roy = roy -1
        elif move == "w": roy = roy +1
    else: print("standstill")

    
    

    for x in boarda:
        if rox == x[0] and roy == x[1]: x[2] = ro
        else: x[2] = sp
    for x in boardb:
        if rox == x[0] and roy == x[1]: x[2] = ro
        else: x[2] = sp
    for x in boardc:
        if rox == x[0] and roy == x[1]: x[2] = ro
        else: x[2] = sp
    for x in boardd:
        if rox == x[0] and roy == x[1]: x[2] = ro
        elif x[0] != 3: x[2] = sp
        else: x[2] = ki
    for x in boarde:
        if rox == x[0] and roy == x[1]: x[2] = ro
        elif x[0] != 0: x[2] = sp
        else: x[2] = wa
    move = input("Input move!")
    print (boarde)
    print (boardd)
    print (boardc)
    print (boardb)
    print (boarda)
    if roy == 3 and rox == 3 or rox == 0 and roy == 4: sp = "."
    if rox == 0 and roy == 4: print("You ran into water!")
    if roy == 3 and rox == 3: print("Robotfindskitten! Yay!")
print ("Game over.")