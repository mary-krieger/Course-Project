# takes user input of number of years
years = float(input("Enter the number of years: "))

#calculates the minutes in a year
minPerYear = 365 * 24 * 60

#Calculates minutes in years given
totalMinutes = years * minPerYear

#prints the results
print("There are", totalMinutes, "minutes in", years, "years.")
