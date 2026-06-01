num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
op = input("Enter an operator (+, -, *, /): ")

numsum = float(num1) + float(num2)
numminus = float(num1) - float(num2)
nummultiply = float(num1) * float(num2)
numdivide = float(num1) / float(num2)

if op=="+":
    print(numsum)

elif op=="-":
    print(numminus)

elif op=="*":
    print(nummultiply)

elif op=="/":
    print(numdivide)
