print(")")
print("(        /(")
print("\yYYy,_I_`;")
print("JgLFO^JL_")
print("\ `-  \, ` ")

number1 = int(input("Input first number"))
number2 = int(input("Input second number"))
operation = input("Input operation (addition, subtraction, multiplication, division)")
if operation == "+": print(number1 + number2)
elif operation == "-": print(number1 - number2)
elif operation == "*": print(number1 * number2)
elif operation == "/": print(number1 / number2)
else: print("Invalid operation!")

noun1 = input("Choose a noun")
pnoun1 = input("Choose a plural noun")
noun2 = input("Choose a noun")
place = input("Choose a place")
adjective = input("Choose an adjective")
print(noun1 + "ate five oranges. " + pnoun1 + "went with " + noun2 + "to go to " + place + "and it was " + adjective)

student = 20
classroom = student * 30
print("pages read by a classroom", classroom)
school = classroom * 12
print("pages school", school)
goal = 10000
pagesperstudent = goal / 360
print("Pages each student ", pagesperstudent)
print(classroom)
print(school)

