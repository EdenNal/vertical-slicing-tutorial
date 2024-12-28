import sys

PROVINCE_TAX_RATES = {
    "ON": 0.13,  # Ontario
}

if len(sys.argv) != 3:
    print("Usage: python mcmerch.py <price> <province_code>")
    sys.exit(1)

try:
    price = float(sys.argv[1])
    province_code = sys.argv[2].upper()
    tax_rate = PROVINCE_TAX_RATES[province_code]

except ValueError:
    print("Please provide a valid number for the price.")
    sys.exit(1)

# Calculate total price
total_price = price * (1 + tax_rate)

print(f"Total price after tax for {province_code}: ${total_price:.2f}")
