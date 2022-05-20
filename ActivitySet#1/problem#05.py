# Functions
#modify using functions
def computepay(h, r):
    if(h>40):
      pay=(40*r + (h-40)*(1.5*r))
    else:
      pay=h*r
    return pay

hrs = float(input("Enter hours? "))
rte = float(input("Enter rate per hour? "))

p = computepay(hrs, rte)
print("Pay", p)
