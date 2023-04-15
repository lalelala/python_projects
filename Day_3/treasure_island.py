print("Welcome to Treasure Island.\n"
"Your mission is to find the treasure.")

step1 = input("Turn left or right?")
if step1 == "left":
    step2 = input("swim across or wait?")
    if step2 == "wait":
        step3 = input("which door? Red, Yellow or Blue?").lower()
        if step3 == "yellow":
            print("You Win!")
        elif step3 == "blue":
            print("Eaten by beasts. Game Over.")
        elif step3 == "red":
            print("Burned by fire. Game Over.")
        else:
            print("Game Over.")        
    else:
        print("Attacked by trout. Game Over.")
else:
    print("Fall into hole. Game over.")




