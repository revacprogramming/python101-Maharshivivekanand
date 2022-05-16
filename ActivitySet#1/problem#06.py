# Loops & Iterators

largest = None
smallest = None
sum = None

while True:
    n = input("Enter a number? ")
    if n == "done":
        break
    try:
        num = int(n)
        if largest is None or num > largest:
            largest = num
        if smallest is None or num < smallest:
            smallest = num
    except:
        print('Invalid input')


print("Maximum is", largest)
print("Minimum is", smallest)
