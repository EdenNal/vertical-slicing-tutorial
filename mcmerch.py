import argparse

def main():
    # Configure CLI arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("price", type=float, help="The price of the item")
    parser.add_argument(
        "--province", 
        type=str, 
        default="Ontario", 
        choices=["Ontario", "Quebec"], 
        help="The province where the tax is applied (default: Ontario)"
    )
    args = parser.parse_args()

    # Set the tax rate based on the province
    if args.province == "Ontario":
        tax_rate = 1.13  # Ontario's tax rate
    elif args.province == "Quebec":
        tax_rate = 1.14975  # Quebec's tax rate

    # Calculate total price with tax
    total = args.price * tax_rate

    print(f"The total price in {args.province} is {total:.2f}")

if __name__ == '__main__':
    main()
