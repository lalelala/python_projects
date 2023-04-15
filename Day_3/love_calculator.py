print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
lovers = name1.lower() + name2.lower()
print(lovers)
t= lovers.count('t')
r = lovers.count('r')
u = lovers.count('u')
e = lovers.count('e')
true = t+r+u+e
#print(f"TRUE: {true}")
l=lovers.count('l')
o=lovers.count('o')
v=lovers.count('v')
e=lovers.count('e')
love= l+o+v+e
#print(f"LOVE: {love}")
score1 = str(true) + str(love)
score = int(score1)
#print(score)
f score <10 or score>90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score<40 or score<50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
