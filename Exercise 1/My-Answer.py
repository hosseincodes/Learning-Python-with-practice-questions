import datetime

#Get name and age
name = input("name: ")
age = int(input("age : "))

#Get the current year
today = datetime.date.today()
year = today.strftime("%Y")

#Age calculations
ageCalculation = int(100) - age
hundredYearsLater = int(ageCalculation) + int(year)

#Display name and year
print("Hi " + name + " You will be 100 years old in " + str(hundredYearsLater))