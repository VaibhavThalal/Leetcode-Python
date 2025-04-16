# Function to perform addition
def add(a, b):
    return a + b

# Function to perform subtraction
def subtract(a, b):
    return a - b

# Function to perform multiplication
def multiply(a, b):
    return a * b

# Function to perform division
def divide(a, b):
    # Check for division by zero
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

# Function to calculate percentage
def percentage(total, value):
    return (value / total) * 100

# Function to calculate modulus
def mod(a, b):
    return a % b

# Function to calculate profit or loss and its percentage
def profit_or_loss(cost_price, selling_price):
    if selling_price > cost_price:
        profit = selling_price - cost_price
        profit_percentage = percentage(cost_price, profit)
        return f"Profit: {profit}, Profit Percentage: {profit_percentage:.2f}%"
    elif selling_price < cost_price:
        loss = cost_price - selling_price
        loss_percentage = percentage(cost_price, loss)
        return f"Loss: {loss}, Loss Percentage: {loss_percentage:.2f}%"
    else:
        return "No Profit, No Loss"

# Main calculator function
def calculator():
    while True:
        # Display the menu of operations
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Percentage")
        print("6. Modulus")
        print("7. Profit or Loss")
        print("Q. Quit")

        # Take user input for operation choice
        choice = input("Enter choice (1/2/3/4/5/6/7/Q): ").strip().upper()

        # Check if the user wants to quit
        if choice == 'Q':
            print("Exiting the calculator. Goodbye!")
            break

        # Check if the choice is valid
        if choice in ['1', '2', '3', '4', '5', '6', '7']:
            if choice in ['1', '2', '3', '4', '6']:
                # Take input for the two numbers
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                # Perform the selected operation and display the result
                if choice == '1':
                    print(f"The result is: {add(num1, num2)}")
                elif choice == '2':
                    print(f"The result is: {subtract(num1, num2)}")
                elif choice == '3':
                    print(f"The result is: {multiply(num1, num2)}")
                elif choice == '4':
                    print(f"The result is: {divide(num1, num2)}")
                elif choice == '6':
                    print(f"The result is: {mod(num1, num2)}")
            elif choice == '5':
                # Take input for total and value
                total = float(input("Enter the total value: "))
                value = float(input("Enter the value: "))
                print(f"The percentage is: {percentage(total, value)}%")
            elif choice == '7':
                # Take input for cost price and selling price
                cost_price = float(input("Enter the cost price: "))
                selling_price = float(input("Enter the selling price: "))
                print(profit_or_loss(cost_price, selling_price))
        else:
            # Handle invalid input
            print("Invalid input. Please select a valid operation.")

# Entry point of the program
if __name__ == "__main__":
    calculator()

