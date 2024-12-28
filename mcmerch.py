import sys

# Check if price argument is provided
if len(sys.argv) != 2:
    print("Usage: python mcmerch.py <price_per_item>")
    sys.exit(1)

try:
    # Read price from command line arguments
    price = float(sys.argv[1])
except ValueError:
    print("Please provide a valid number for the price.")
    sys.exit(1)

# Ontario tax rate
ON_TAX_RATE = 0.13

# Calculate the total price
total_price = price * (1 + ON_TAX_RATE)

# Print the resulting price
print(f"Total price after tax: ${total_price:.2f}")
