num1 = float(input("Enter number 1: "))
num2 = float(input("Enter number 2: "))
act = str(input("Choose action: Add(a), Sub(s), Mult(m), Div(d): "))

print("The result is: ", end="")
if act == "a":
    print(num1 + num2)
elif act == "s":
    print(num1 - num2)
elif act == "m":
    print(num1 * num2)
else:
    print(num1 / num2)