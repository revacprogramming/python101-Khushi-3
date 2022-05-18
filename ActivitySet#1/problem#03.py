# Variables, Expressions & Statements
def main():
  hrs = input("Enter hours: ")
  rate=input("enter Rate:")
  total=compute(hrs,rate)
  return output(total)
  
def compute(hrs,rate):
  h=float(hrs)
  r=float(rate)
  pay=h*r
  return pay
def output(total):
  return print("the pay is:",total)


main()