def loan_payment_calc():
    print("This is the monthly Loan payment calculator")
    print("")
    principal = float(input("Enter the principal amount : "))
    interest = float(input("Enter the interest rate : "))
    years = int(input("Enter the number of years : "))
    total_months = years*12
    monthly_interest = interest/1200
    loan_payment = principal*monthly_interest/(1-(1+monthly_interest)**(-total_months))
    print("Monthly loan payment is : "+ str(loan_payment))

loan_payment_calc()
