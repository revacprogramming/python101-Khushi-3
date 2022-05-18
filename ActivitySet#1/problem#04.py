# Conditional Execution
def main():
  hrs = input("Enter hours:")
  rate=input("Enter the Rate:")
  compute(hrs,rate)
def compute(hrs,rate):
  h=float(hrs)
  r=float(rate)
  if h>40:
    pay=(40*r+(h-40)*(1.5*r))
  else:
    pay=h*r
  print(pay)

main()
