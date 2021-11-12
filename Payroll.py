print("\n\n\n           Payroll for Multiple Employees")
print("----------------------------------------------------\n")
count = int(input("Enter the Number of Employees : "))

for i in range(count):
    print("\n----------------------------------------------------\n")
    EmployeesName = input("Enter Employee Name : ")
    RegularHours = int(input("Enter Regular Hours Worked: "))
    OtHours = int(input("Enter Overtime Hours Worked: "))
    PayRate = int(input("Enter Hourly Pay Rate: "))
    TotalHours = RegularHours + OtHours
    OtPay = OtHours * PayRate * 1.6
    RegularPay = RegularHours * PayRate
    GrossPay = RegularPay + OtPay

    if GrossPay >=0 and GrossPay <=10000:
        Tax = GrossPay * 0.05
    elif GrossPay >=10001 and GrossPay <=30000:
        Tax = GrossPay * 0.10
    elif GrossPay >=30001 and GrossPay <=70000:
        Tax = GrossPay * 0.15
    elif GrossPay >=70001 and GrossPay <=140000:
        Tax = GrossPay * 0.20
    elif GrossPay >=140001 and GrossPay <=250000:
        Tax = GrossPay * 0.25
    elif GrossPay >=250001 and GrossPay <=500000:
        Tax = GrossPay * 0.30
    elif GrossPay >=500001:
        Tax = GrossPay * 0.35

    PhilHealth = GrossPay * 0.015
    SSS = 1125
    Pagibig = 100
    TotalDeduc = Tax + PhilHealth + SSS + Pagibig
    NetPay = GrossPay - TotalDeduc

    if(TotalHours < 0):
        print("\n----------------------------------------------------\n")
        print("Invalid Total hours worked, it must be greater than 1")
    elif(TotalHours > 0):
            print("\n----------------------------------------------------\n")
            print("Your Overtime Pay is: ", OtPay)
            print("Your Regular Pay is: ", RegularPay)
            print("Your Gross Pay is: ", GrossPay)
            print("\n----------------------------------------------------\n")
            print("Deductions:")
            print("Tax Deduction: ", Tax)
            print("SSS Contribution: ", SSS)
            print("PhilHealth Deduction: ", PhilHealth)
            print("Pagibig Deduction: ", Pagibig)
            print("\n----------------------------------------------------\n")
            print("Total Deductions: ", TotalDeduc)
            print("Net Pay: ", NetPay)
            print("\n----------------------------------------------------\n")