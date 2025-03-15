
employeeFName = str(input ("Enter employee first name"))
employeeLName = str(input ("Enter employee last name"))
employeeID = int(input ("Enter employeeID"))
numDependent = int(input ("Enter numDependent"))
hoursWorked = int(input ("Enter hoursWorked"))
otHours = int(input("Enter OT'"))
payRate = float(input ("Enter payRate"))


if hoursWorked <= 40:
        grossPay = float((hoursWorked * payRate))
        
else:
       regPay = float((hoursWorked-otHours) * payRate)
       overPay = float(otHours * (1.5 * payRate))
       grossPay = float(overPay + regPay)

if  numDependent != 0:
    preTaxPay =  float(grossPay - (25 * numDependent))

else:
    preTaxPay = float(grossPay)
    
sTax = float(0.056 * preTaxPay)
fTax = float(0.079 * preTaxPay)
postTaxPay = float(preTaxPay - sTax - fTax)

print (employeeFName, employeeLName,"'s", "Gross Pay is $", grossPay, "Pre-Tax Pay is $", preTaxPay, "Post Tax pay is $", postTaxPay)
