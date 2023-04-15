age = input("What is your age? ")

left = 90 - int(age)
days = left*365
weeks = left*52
months = left*12
message = f"You have {days} days, {weeks} weeks and {months} months left till you are 90 years old."

print(message)
