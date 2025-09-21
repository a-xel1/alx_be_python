numb1 = float(input("Enter the first number: "))
numb2 = float(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

if operation == "+":
    addition = numb1 + numb2
    print(f"The result is {addition}.")
elif operation == "-":
    subtraction = numb1 - numb2
    print(f"The result is {subtraction}.")
elif operation == "*":
    multiplication = numb1 * numb2
    print(f"The result is {multiplication}.")
elif operation == "/":
    if numb2 == 0:
        print("Cannot divide by zero.")
    else:
        division = numb1 / numb2
        print(f"The result is {division}.")
else:
  print("Invalid operation. Please choose +, -, *, /")
  
