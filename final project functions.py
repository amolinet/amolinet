def grossPay( hoursWorked: int, otHours: float, payRate: float):
    if hoursWorked <= 40:
        grossPay = ((hoursWorked * payRate))
        print("Gross Pay is ", grossPay)
    else:
       regPay = ((hoursWorked-otHours) * payRate)
       overPay = (otHours * (1.5 * payRate))
       grossPay = (overPay + regPay)
       print( "Gross Pay is ",  grossPay)


def preTaxPay( grossPay: float, numDependent: int):
    if  numDependent != 0:
       preTaxPay =  float(grossPay - (25 * numDependent))
       print ("Pre Tax Pay is" , preTaxPay)
    else:
        preTaxPay = float(grossPay)
        print ("Pre Tax Pay is" , preTaxPay)

def postTaxPay( preTaxPay: float):
    sTax = float(0.056 * preTaxPay)
    fTax = float(0.079 * preTaxPay)
    postTaxPay = float(preTaxPay - sTax - fTax)
    print("Post Tax Pay is " , postTaxPay)
