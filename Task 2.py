# Stock Portfolio Tracker

# Predefined stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 175,
    "MSFT": 420
}

portfolio = []
total_investment = 0

print("=" * 40)
print("       STOCK PORTFOLIO TRACKER")
print("=" * 40)

print("\nAvailable Stocks:")

for stock, price in stock_prices.items():
    print(f"{stock}: ${price}")

try:
    number = int(input("\nHow many stocks do you want to add? "))

    if number <= 0:
        print("Please enter a positive number.")
    else:
        for i in range(number):

            print(f"\nStock Entry {i + 1}")

            stock_name = input("Enter stock symbol: ").upper().strip()

            if stock_name not in stock_prices:
                print("Stock not available. Skipping entry.")
                continue

            quantity = int(input("Enter quantity: "))

            if quantity <= 0:
                print("Quantity must be positive. Skipping entry.")
                continue

            price = stock_prices[stock_name]
            investment = price * quantity

            total_investment += investment

            portfolio.append({
                "Stock": stock_name,
                "Quantity": quantity,
                "Price": price,
                "Investment": investment
            })

        print("\n" + "=" * 40)
        print("          PORTFOLIO SUMMARY")
        print("=" * 40)

        if portfolio:
            for item in portfolio:
                print(f"\nStock: {item['Stock']}")
                print(f"Quantity: {item['Quantity']}")
                print(f"Price: ${item['Price']}")
                print(f"Investment: ${item['Investment']:.2f}")

            print("\nTotal Investment Value: "
                  f"${total_investment:.2f}")

            # Save portfolio to a text file
            with open("portfolio_summary.txt", "w") as file:
                file.write("STOCK PORTFOLIO SUMMARY\n")
                file.write("=" * 30 + "\n")

                for item in portfolio:
                    file.write(
                        f"{item['Stock']} | "
                        f"Quantity: {item['Quantity']} | "
                        f"Price: ${item['Price']} | "
                        f"Investment: ${item['Investment']:.2f}\n"
                    )

                file.write(
                    f"\nTotal Investment: ${total_investment:.2f}"
                )

            print("\nPortfolio saved to portfolio_summary.txt")

        else:
            print("No valid stock entries were added.")

except ValueError:
    print("Invalid input. Please enter numerical values.")

print("\nThank you for using Stock Portfolio Tracker!")
