# Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay should be the normal rate for hours up to 40 and time-and-a-half for the hourly rate for all hours worked above 40 hours. Put the logic to do the computation of pay in a function called computepay() and use the function to do the computation. The function should return a value. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use input to read a string and float() to convert the string to a number. Do not worry about error checking the user input unless you want to - you can assume the user types numbers properly. Do not name your variable sum or use the sum() function.
#modified
def main():
  hrs = float(input("Enter hours: "))
  rate = float(input("Enter rate per hour: "))
  p = computepay(hrs, rate)
  print("Pay", p)
  
def computepay(h, r):
    if(h>40):
      pay=(40*r + (h-40)*(1.5*r))
    else:
      pay=h*r
    return pay
main()





"""
largest = None
smallest = None

while True:
    num = input("Enter a number? ")

    if num == "done":
        break
    try:
      n=int(num)
    except:
      print("invalid")
      continue
    if largest is None or largest<n:
      largest=n
    elif smallest is None or smallest>n:
      smallest=n

    print(n)

print("Maximum", largest)
print("Mninimum",smallest)"""
