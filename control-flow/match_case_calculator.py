numb1 = float(input("Enter the first number: "))
numb2 = float(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

match operation:
    case "+":
        addition = numb1 + numb2
        print(f"The result is {addition}.")
    case "-":
        subtraction = numb1 - numb2
        print(f"The result is {subtraction}.")
    case "*":
        multiplication = numb1 * numb2
        print(f"The result is {multiplication}.")
    case "/":
        if numb2 == 0:
            print("Cannot divide by zero.")
        else:
            division = numb1 / numb2
            print(f"The result is {division}.")
else:
  print("Invalid operation. Please choose +, -, *, /")
  
