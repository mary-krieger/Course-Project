# Takes users input for population, growth rate, number of hours to achieve rate, and number of hours population grows.
initialPopulation = float(input("Enter the initial population."))
growthRate = float(input("Enter the rate of growth(a real number greater than 0)."))
numHours = float(input("Enter the number of hours to achieve this growth rate."))
totalHours = float(input("Enter the total number of hours the population grows."))

# Find the number of growth periods
growthPeriods = int(totalHours / numHours)

# Initialize the population
population = initialPopulation

# Loop through each growth period
for eachPass in range(growthPeriods):
    population *= growthRate

# Print results
print("The predicted population after", totalHours, "hours is:", population,".")
