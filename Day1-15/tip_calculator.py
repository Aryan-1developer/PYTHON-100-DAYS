print("tip calculator project")
bill = float(input("enter the total bill amount"))
percentage=float(input("enter the percentage of bill you would want to tip"))
tip = bill*(percentage/100)
total_bill= bill + tip
print(f"the total bill is {total_bill}")

