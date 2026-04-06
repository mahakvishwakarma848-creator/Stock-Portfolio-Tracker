stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 300
}

total = 0

print("Stock Portfolio Tracker")
while True:
    stock = input("Enter stock name (or 'done'): ").upper()
    if stock == "DONE":
        break

    if stock in stocks:
        qty = int(input("Enter quantity: "))
        total += stocks[stock] * qty
    else:
        print("Stock not found!")

print("Total Investment Value:", total)

# Save to file
with open("portfolio.txt", "w") as f:
    f.write(f"Total Investment: {total}")