print ("welcome to tip calculator")
total_bill = input("what was your total bill")
total_bill_float = float(total_bill)
percentage_bill = input("what percentage of bill would you like to tip 10 15 18")
percentage_bill_float = float(percentage_bill)
tip_calculator = (percentage_bill_float / 100) *total_bill_float
message = f"Your total tip is {tip_calculator:.2f}"
# here :.2f is used to display info. upto 2 decimal points
print(message)
