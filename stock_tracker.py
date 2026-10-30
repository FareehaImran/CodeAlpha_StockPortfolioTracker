# Hardcoded stock prices (USD)
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 130,
}


def show_available_stocks():
    print("\nAvailable stocks:")
    for name, price in STOCK_PRICES.items():
        print(f"  {name}: ${price}")


def get_portfolio():

    portfolio = {}

    while True:
        name = input("\nEnter stock name (or 'done' to finish): ").upper().strip()

        if name == "DONE":
            break

        if name not in STOCK_PRICES:
            print("Stock not found. Please choose from the list above.")
            continue

        quantity_text = input(f"How many shares of {name}? ").strip()

        if not quantity_text.isdigit() or int(quantity_text) <= 0:
            print("Please enter a whole number greater than 0.")
            continue

        quantity = int(quantity_text)

        # If the stock was already added, increase its quantity
        portfolio[name] = portfolio.get(name, 0) + quantity
        print(f"Added {quantity} share(s) of {name}.")

    return portfolio


def calculate_total(portfolio):
    """Returns the total value and a list of (name, qty, price, value) rows."""
    rows = []
    total = 0
    for name, quantity in portfolio.items():
        price = STOCK_PRICES[name]
        value = price * quantity
        total += value
        rows.append((name, quantity, price, value))
    return total, rows


def show_summary(rows, total):
    print("\n" + "=" * 45)
    print(f"{'Stock':<8}{'Qty':>6}{'Price':>10}{'Value':>12}")
    print("-" * 45)
    for name, quantity, price, value in rows:
        print(f"{name:<8}{quantity:>6}{'$' + str(price):>10}{'$' + str(value):>12}")
    print("-" * 45)
    print(f"{'Total investment:':<24}{'$' + str(total):>21}")
    print("=" * 45)


def save_to_file(rows, total):
    filename = "portfolio.txt"
    with open(filename, "w") as file:
        file.write("STOCK PORTFOLIO SUMMARY\n")
        file.write("-" * 30 + "\n")
        for name, quantity, price, value in rows:
            file.write(f"{name}: {quantity} x ${price} = ${value}\n")
        file.write("-" * 30 + "\n")
        file.write(f"Total investment: ${total}\n")
    print(f"\nSaved to {filename}")


def main():
    print("=== STOCK PORTFOLIO TRACKER ===")
    show_available_stocks()

    portfolio = get_portfolio()

    if not portfolio:
        print("\nNo stocks entered. Goodbye!")
        return

    total, rows = calculate_total(portfolio)
    show_summary(rows, total)

    choice = input("\nSave result to a file? (y/n): ").lower().strip()
    if choice == "y":
        save_to_file(rows, total)

    print("Thank you for using the tracker!")


if __name__ == "__main__":
    main()