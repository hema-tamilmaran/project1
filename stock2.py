# Hardcoded stock prices (you can expand this dictionary)
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2800,
    "AMZN": 3500,
    "MSFT": 310
}

# Store user's stock data
user_stocks = {}

# Input loop
while True:
    stock_name = input("Enter stock symbol (or type 'done' to finish): ").upper()
    if stock_name == 'DONE':
        break
    if stock_name not in stock_prices:
        print(f"Stock '{stock_name}' not found in price list.")
        continue

    try:
        quantity = int(input(f"Enter quantity for {stock_name}: "))
        if quantity < 0:
            print("Quantity must be non-negative.")
            continue
        user_stocks[stock_name] = user_stocks.get(stock_name, 0) + quantity
    except ValueError:
        print("Please enter a valid number.")

# Calculate total investment
total_investment = 0
print("\n--- Investment Summary ---")
for stock, qty in user_stocks.items():
    price = stock_prices[stock]
    investment = price * qty
    total_investment += investment
    print(f"{stock}: {qty} x ${price} = ${investment}")

print(f"\nTotal Investment Value: ${total_investment}")

# Ask to save to file
save = input("\nDo you want to save this summary to a file? (yes/no): ").lower()
if save == 'yes':
    filename = input("Enter filename (e.g., 'investment_summary.txt' or '.csv'): ")
    with open(filename, 'w') as file:
        file.write("Stock,Quantity,Price,Investment\n")
        for stock, qty in user_stocks.items():
            price = stock_prices[stock]
            investment = price * qty
            file.write(f"{stock},{qty},{price},{investment}\n")
        file.write(f"\nTotal Investment,,,{total_investment}")
    print(f"Summary saved to '{filename}'")
