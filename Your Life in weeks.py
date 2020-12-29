# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

# age_as_int is the oldest you will be in this case, 90
age_as_int = 90

# years is referring to how many years you have left based on your current age
years = (int(age_as_int) - int(age))

# days refers to how many days you have left until you reach 90
days = (365*years)

# How many weeks you have left until you reach 90
weeks = (52 * years)

# How many months you have left until you reach 90
months = (12 * years)

print(f"You have {days} days,  {weeks} weeks, and {months} months left ")
