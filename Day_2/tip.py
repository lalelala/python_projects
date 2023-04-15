print("Welcome to the tip calculator.")

bill = int(input("What was the bill? ")
people = int(input("How many people to split by? ")
tip = int(input("What percentage tip do you want to give? ")

tip_amount = bill*(tip/100)
total = ((bill + tip_amount)/people)
round_total = round(total, 2)

print(f"You each pay {round_total}.")
