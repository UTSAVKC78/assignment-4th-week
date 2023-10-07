def computepay(hours, rate):
    if hours <= 40:
        pay = hours * rate
    else:
        regular_pay = 40 * rate
        overtime_hours = hours - 40
        overtime_pay = overtime_hours * 1.5 * rate
        pay = regular_pay + overtime_pay
    return pay

try:
    hours = float(input("enter the number of hours worked: "))
    rate = float(input("enter the hourly rate: "))
    
    if hours < 0 or rate < 0:
        print("error: hours and rate must be non-negative.")
    else:
        salary = computepay(hours, rate)
        print(f"Salary: {salary:.2f}")
except valueError:
    print("Error: invalid input. please enter numeric values for hours and rate.")

