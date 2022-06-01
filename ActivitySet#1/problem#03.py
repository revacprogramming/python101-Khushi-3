#Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Use 35 hours and a rate of 2.75 per hour to test the program (the pay should be 96.25). You should use input to read a string and float() to convert the string to a number. Do not worry about error checking or bad user data.
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