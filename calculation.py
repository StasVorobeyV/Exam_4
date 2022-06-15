print("ноль в качестве знака: ")
x = float(input("x="))
y = float(input("y="))

while True:
    s = input("знак(+, -, *, /):")

    if s == 0:
            break
    elif s == '+':
        print(x + y)
    elif s == "*":
        print(x * y)
    elif s == "/":
        if y != / 0:
            print(x / y)
        else:
            print("деление на ноль!")