#Declarations of variables
loan = 0
interestRate = 0
yearsLoan = 0
monthlyPayment = 0
numberPayments = 0

#User input
strLoan = input("Enter the cost of the loan: ")
strInterest = input("Enter the interest rate: ")
strYears = input("Enter the number of years for the loan: ")

#Convert the variables for friendly use
loan = float(strLoan)
interestRate = float(strInterest)
yearsLoan = float(strYears)

#We need to know how many months you will be paid the loan
numberPayments = yearsLoan*12

#We use this little formula to calculate the monthly payment
monthlyPayment = (loan * interestRate * (1 + interestRate ) * numberPayments) \
                / ((1 + interestRate) * numberPayments - 1)

#We print the result with only two decimal
print("Yout monthly payment will be %.2f" %monthlyPayment)

