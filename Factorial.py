num = int(input("Enter the value:"))

factorial = 1

if num<0:
    print("factorial cannot be less that 0")
elif num==0:
    print("factorial of 0 is 1")
else:
    for i in range(1,num+1):
        factorial=factorial*i
        print("the factorial of",num,"is",factorial)
