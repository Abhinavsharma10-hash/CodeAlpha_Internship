# ------------------------------
# TASK 2: Stock Portfolio Tracker
# ------------------------------

# Hardcoded dictionary of stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 320
}

# Ask for user's name
name = input("Enter your name: ")

# Welcome message
print(f"\nWelcome {name}! Let's track your stock portfolio.\n")
print("Available stocks and their prices:")
for stock, price in stock_prices.items():
    print(f"{stock}: ${price}")

# Initialize total investment
total_value = 0
portfolio = {}

# Get user input for stock quantities
while True:
    stock_name = input("\nEnter stock symbol (or 'done' to finish): ").upper()

    if stock_name == "DONE":
        break

    if stock_name in stock_prices:
        try:
            quantity = int(input(f"Enter quantity of {stock_name}: "))
            portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity
            total_value += stock_prices[stock_name] * quantity
        except ValueError:
            print("Invalid quantity! Please enter a number.")
    else:
        print("Stock not found in list.")

# Display result
print("\nYour Stock Portfolio:")
for stock, qty in portfolio.items():
    print(f"{stock} - Quantity: {qty}, Value: ${stock_prices[stock] * qty}")

print(f"\nTotal Investment Value: ${total_value}")

# Ask if user wants to save the portfolio
save_option = input("\nDo you want to save the portfolio to a file? (yes/no): ").lower()

if save_option == "yes":
    file_name = f"{name}_portfolio.txt"
    with open(file_name, "w") as file:
        file.write(f"Stock Portfolio for {name}\n")
        file.write("-" * 30 + "\n")
        for stock, qty in portfolio.items():
            file.write(f"{stock} - Quantity: {qty}, Value: ${stock_prices[stock] * qty}\n")
        file.write(f"\nTotal Investment Value: ${total_value}\n")
    print(f"Portfolio saved to '{file_name}' successfully!")

print("\nThank you for using Stock Portfolio Tracker!")
