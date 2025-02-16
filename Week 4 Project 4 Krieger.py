# User inputs for intial height and number of bounces
initialHeight = float(input("Enter the initial height from which the ball is dropped."))
numBounces = int(input("Enter the number of times the ball is allowed to continure bouncing."))

# Delcare bounce index
bounceIndex = 0.6
totalDistance = 0

# For loop to calculate the distance traveled in per bounce
for eachPass in range(numBounces):
    calcDistance = initialHeight * bounceIndex
    totalDistance = totalDistance + calcDistance + initialHeight
    initialHeight = calcDistance


print("After", numBounces, "bounces, the ball traveled", totalDistance, "feet.")
    
    
