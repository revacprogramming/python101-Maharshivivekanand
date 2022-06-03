
def add(a, b):
    sum=a+b
    return sum

def output(a, b, sum):
    print(f"the sum of {a} and {b} is {sum}")
    pass 
def input_two_numbers():
    a=int(input())
    b=int(input())
    return a,b

def main():
    a, b = input_two_numbers()
  =
    sum = add(a,b)
  

    output(a, b, sum)


if __name__ == '__main__':
    main()
