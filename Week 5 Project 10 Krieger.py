purchasePrice = float(input("Enter the purchase price: $ "))
downPayment = .1 * purchasePrice
annualRate = .12
monthlyRate = annualRate / 12
balance = purchasePrice - downPayment
monthlyPayment = .05 * purchasePrice
month = 1
print("Month    Starting Balace    Interest to Pay    Payment    Ending Balance")
while balance > 0:
    if monthlyPayment > balance:
        monthlyPayment = balance
        interest = 0
    else:
        interest = balance * annualRate / 12
    principal = monthlyPayment - interest
    remaining = balance - monthlyPayment
    print("%2d%15.2f%15.2f%17.2f%17.2f%17.2f" % (month, balance, interest, principal, monthlyPayment, remaining))
    balance = remaining
    month += 1
