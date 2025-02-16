# Gets employee's input of wage and hours worked
hourlyWage = float(input("Enter your hourly wage: $"))
regularHours = float(input("Enter number of regular hours worked: "))
overtimeHours = float(input("Enter number of overtime hours: "))

# Calculates the regular pay
regularPay = hourlyWage * regularHours

# Calculates overtime pay
overtimePay = hourlyWage * 1.5 * overtimeHours

# Calculates total weekly pay
totalWeeklyPay = regularPay + overtimePay

# Prints the employee's total weekly pay
print("The employee's total weekly pay is $", totalWeeklyPay, ".")
