# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 2800,
    "MSFT": 330,
    "AMZN": 130
}

# Store user stock data
portfolio = {}

# Take user input
while True:
    stock = input("Enter stock symbol (or 'done' to finish): ").upper()
    if stock == 'DONE':
        break
    if stock not in stock_prices:
        print("Stock not found in our price list.")
        continue
    try:
        quantity = int(input(f"Enter quantity for {stock}: "))
        portfolio[stock] = portfolio.get(stock, 0) + quantity
    except ValueError:
        print("Please enter a valid number.")

# Calculate total investment
total_investment = 0
print("\nInvestment Summary:")
print("-------------------")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = qty * price
    total_investment += value
    print(f"{stock}: {qty} shares × ${price} = ${value}")

print(f"\nTotal Investment Value: ${total_investment}")

# Option to save to file
save = input("\nDo you want to save this to a file? (yes/no): ").lower()
if save == 'yes':
    file_type = input("Save as .txt or .csv? ").lower()
    if file_type == 'txt':
        with open("investment_summary.txt", "w") as f:
            for stock, qty in portfolio.items():
                f.write(f"{stock}: {qty} shares × ${stock_prices[stock]} = ${qty * stock_prices[stock]}\n")
            f.write(f"\nTotal Investment Value: ${total_investment}\n")
        print("Saved as investment_summary.txt")
    elif file_type == 'csv':
        with open("investment_summary.csv", "w") as f:
            f.write("Stock,Quantity,Price,Value\n")
            for stock, qty in portfolio.items():
                price = stock_prices[stock]
                value = qty * price
                f.write(f"{stock},{qty},{price},{value}\n")
            f.write(f"Total,,,{total_investment}\n")
        print("Saved as investment_summary.csv")
    else:
        print("Unsupported file type. Skipping save.")
