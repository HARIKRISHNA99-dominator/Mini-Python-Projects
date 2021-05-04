def add(a, b):
    return a + b
def subtract(a, b):
    return a - b

def multiply(a, b):
    return a *b

def divide(a,b):
    return a/b
print("Select the  operation given below")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
while True:
    enter = input("Enter choice within (1 / 2 / 3 / 4)  : ")
    if enter in ('1', '2', '3', '4'):
        x = int(input("Enter the first number  :"))
        y = int(input("Enter the second number   :"))
        if enter == '1':
            print(x,"+",y, "=", add(x, y))
        elif enter == '2':
            print(x,"-",y, "=", subtract(x, y))
        elif enter == '3':
            print(x,"*",y, "=", multiply(x, y))
        elif enter == '4':
            print(x,"/",y, "=", divide(x, y))
        break
    else:
        print("enter a valid input")