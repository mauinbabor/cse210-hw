import csv
from datetime import datetime

def read_csv_file(filename):
    """
    Reads a CSV file and returns its content as a dictionary or list.
    Raises FileNotFoundError and PermissionError if file access fails.
    """
    try:
        with open(filename, mode="r") as file:
            reader = csv.reader(file)
            data = {rows[0]: rows[1:] for rows in reader}
            return data
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
        raise
    except PermissionError:
        print(f"Error: Insufficient permissions to access {filename}.")
        raise

def calculate_receipt(products, requests):
    """
    Generates receipt details based on product catalog and customer requests.
    """
    try:
        subtotal = 0
        total_items = 0
        receipt_lines = []

        for request_id, request_details in requests.items():
            if request_id not in products:
                raise KeyError(f"Error: Unknown product ID {request_id}.")
            
            product_name, product_price = products[request_id]
            quantity = int(request_details[0])
            price = float(product_price)
            item_total = quantity * price

            total_items += quantity
            subtotal += item_total

            receipt_lines.append(f"{product_name}: {quantity} @ {product_price}")

        sales_tax = round(subtotal * 0.06, 2)
        total_due = round(subtotal + sales_tax, 2)

        return receipt_lines, total_items, subtotal, sales_tax, total_due

    except KeyError as e:
        print(e)
        raise

def print_receipt(receipt_lines, total_items, subtotal, sales_tax, total_due):
    """
    Prints the formatted receipt to the terminal.
    """
    print("\nInkom Emporium")
    for line in receipt_lines:
        print(line)

    print(f"\nNumber of Items: {total_items}")
    print(f"Subtotal: {subtotal:.2f}")
    print(f"Sales Tax: {sales_tax:.2f}")
    print(f"Total: {total_due:.2f}")

    print("\nThank you for shopping at the Inkom Emporium.")
    current_date_and_time = datetime.now()
    print(f"{current_date_and_time:%a %b %d %Y %I:%M:%S %p}")

def main():
    try:
        products = read_csv_file("products.csv")
        requests = read_csv_file("request.csv")
        
        receipt_lines, total_items, subtotal, sales_tax, total_due = calculate_receipt(products, requests)
        print_receipt(receipt_lines, total_items, subtotal, sales_tax, total_due)

    except (FileNotFoundError, PermissionError):
        print("Please ensure all required files are present and accessible.")
    except KeyError as e:
        print("A KeyError occurred:", e)
    except Exception as e:
        print("An unexpected error occurred:", e)

if __name__ == "__main__":
    main()

