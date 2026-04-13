while True:
    try:
        oper = input(
            "Enter operation (+, -, *, /) or 'exit' to quit: ").strip()
        if oper == "exit":
            break
        if oper not in ["+", "-", "*", "/"]:
            print("Invalid operation")
            continue
        num_1 = float(input("Enter number 1: "))
        num_2 = float(input("Enter number 2: "))
        if oper == "+":
            result = num_1 + num_2
        elif oper == "-":
            result = num_1-num_2
        elif oper == "/":
            result = num_1/num_2
        elif oper == "*":
            result = num_1*num_2
        else:
            print("Enter the right operation")
        print("Result:", result)
    except ValueError:
        print("Invalid input: please enter numeric values only.")
    except ZeroDivisionError:
        print("Can't be divided by Zero")
