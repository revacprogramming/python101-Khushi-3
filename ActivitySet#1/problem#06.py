# Loops & Iterators
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
print("Mninimum",smallest)
