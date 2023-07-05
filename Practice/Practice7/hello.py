def perform_operation(num1, num2, operation):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        result = num1 / num2
    else:
        print("Invalid operation")
        return None
    
    return result

result = perform_operation(5, 3, '+')
print(result)
