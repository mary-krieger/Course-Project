startingSalary = float(input("Enter the starting salary: $ "))
percentIncrease = float(input("Enter the annual percent increase: "))
years = int(input("Enter the number of years: "))
for i in range(1, years + 1):
    print("Year", i, ", Salary: ", startingSalary * ((1 + percentIncrease) ** (i-1)))
    
