print("\n\n\n           Payroll for Multiple Employees")
print("----------------------------------------------------")
count = int(input("Enter the Number of Employees : "))

for i in range(count):
    print("\n----------------------------------------------------")
    EmployeesName = input("Enter Employee Name : ")
    RegularHours = int(input("Enter Regular Hours Worked: "))
    OtHours = int(input("Enter Overtime Hours Worked: "))
    PayRate = int(input("Enter Hourly Pay Rate: "))
    TotalHours = RegularHours + OtHours
    OtPay = OtHours * PayRate * 1.6
    RegularPay = RegularHours * PayRate

    if(TotalHours < 0):
        print("\n----------------------------------------------------\n")
        print("Invalid Total hours worked, it must be greater than 1")
    elif(TotalHours > 0):
            print("\n----------------------------------------------------\n")
            print("Your Overtime Pay is: ", OtPay)
            print("Your Regular Pay is: ", RegularPay)
            print("Your Gross Pay is: ", OtPay + RegularPay)