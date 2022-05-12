# Conditional Execution

hrs = float(input("Enter hours:"))
rate=float(input("Enter the Rate:"))
if hrs>40:
  pay=(40*rate+(hrs-40)*(1.5*rate))
else:
  pay=hrs*rate
print(pay)
