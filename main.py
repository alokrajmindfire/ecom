"""
Product Processing and Ordering System
--------------------------------------
Handles:
- Multithreaded product loading
- Safe file writing with locks
- Logging and error handling
- CLI-based product ordering
"""
import logging
import threading
import models as mx

logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

file_lock = threading.Lock()

def create_product(data):
    """Create product instance based on category."""
    try:
        pro_id, name, category, price, stock = data
        price = float(price)
        stock = int(stock)
        if category == "Electronics":
            return mx.Electronics(pro_id, name, category, price, stock)
        elif category == "Clothing":
            return mx.Clothing(pro_id, name, category, price, stock)
        else:
            return mx.Product(pro_id, name, category, price, stock)
    except ValueError as err:
        logging.error("Data type conversion error for %s: %s", data, err)
    except (OSError, IOError) as err:
        logging.error("Error creating product from data %s: %s", data, err)
    return None

def write_product(data):
    """Thread-safe file write for product information."""
    with file_lock:
        try:
            with open('final.txt', 'a',  encoding='utf-8') as file:
                file.write(data + '\n')
        except (OSError, IOError) as err:
            logging.error("Error writing data to file: %s", err)

def process_product(data, products_list):
    """Create product, calculate totals, and write to file"""
    product = create_product(data)
    if product:
        try:
            total = product.calculate_price()
            totalv = product.calculate_total()
            para = ",".join([
                product.pro_id,
                product.name,
                product.category,
                str(product.price),
                str(product.stock),
                str(total),
                str(totalv)
            ])
            write_product(para)
        except (OSError, IOError) as err:
            logging.error("Error calculating totals for product %s: %s", product.pro_id, err)
        products_list.append(product)

def load_products(file_path):
    """Load products from file using multithreading"""
    products = []
    threads = []

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line_number, line in enumerate(file, start=1):
                data = line.strip().split(',')
                if len(data) == 5:
                    t = threading.Thread(target=process_product, args=(data, products))
                    threads.append(t)
                    t.start()
                else:
                    logging.warning("Line %d malformed: %s", line_number, line.strip())

        for t in threads:
            t.join()

    except FileNotFoundError:
        logging.error("File not found: %s",file_path)
    except (OSError, IOError) as e:
        logging.error("Error loading products from %s %s",file_path,e)

    return products

def write_order(order_data):
    """Thread-safe order write"""
    with file_lock:
        try:
            with open('order_history.txt', 'a', encoding='utf-8') as file:
                file.write(order_data + '\n')
        except (OSError, IOError) as err:
            logging.error("Error writing order to file: %s", err)

def main():
    """main function to process order"""
    filename = input("Enter product file name: ")
    products = load_products(filename)

    if not products:
        print("No products loaded.")
        return

    user_name = input("Enter your name: ").strip()
    user_email = input("Enter your email: ").strip()
    user = mx.User(user_name, user_email)

    print("\nAvailable Products:")
    for prod in products:
        print(f"ID: {prod.pro_id} | Name: {prod.name} | Category: {prod.category} | Price: {prod.price} | Stock: {prod.stock}")

    order_id = input("\nEnter the product ID to order: ").strip()
    selected_product = next((p for p in products if p.pro_id == order_id), None)

    if selected_product:
        quantity = int(input(f"Enter quantity to order (Available: {selected_product.stock}): "))
        if quantity > selected_product.stock:
            print("Not enough stock available.")
            logging.warning("User %s tried to order invalid product ID: %s", user.name, order_id)
            return

        total_price = selected_product.price * quantity
        if isinstance(selected_product, mx.Electronics):
            total_price += 0.15 * total_price
        elif isinstance(selected_product, mx.Clothing):
            total_price -= 0.10 * total_price

        selected_product.stock -= quantity
        order_data = f"{user.name},{user.email},{selected_product.pro_id},{selected_product.name},{quantity},{total_price:.2f}"
        write_order(order_data)

        print(f"Order placed successfully! Total price: ${total_price:.2f}")
        logging.info("Order placed: %s", order_data)
    else:
        print("Product ID not found.")
        logging.warning("User %s tried to order invalid product ID: %d",user.name,order_id)

if __name__ == "__main__":
    main()