import models as mx
import logging

logging.basicConfig(
    filename='app.log', 
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def create_product(data):
    try:
        id, name, category, price, stock = data
        price = float(price)
        stock = int(stock)
        if category == "Electronics":
            return mx.Electronics(id, name, category, price, stock)
        elif category == "Clothing":
            return mx.Clothing(id, name, category, price, stock)
        else:
            return mx.Product(id, name, category, price, stock)
    except ValueError as ve:
        logging.error(f"Data type conversion error for {data}: {ve}")
    except Exception as e:
        logging.error(f"Error creating product from data {data}: {e}")
    return None

def write_product(data):
    try:
        with open('final.txt', 'a') as file:
            file.write(data + '\n')
    except Exception as e:
        logging.error(f"Error writing data to file: {e}")

def load_products(file_path):
    products=[]
    try:
        with open(file_path, 'r') as file:
            for line_number, line in enumerate(file, start=1):
                data = line.strip().split(',')
                if len(data) == 5:
                    product = create_product(data)
                    products.append(product)
                    if product:
                        try:
                            total = product.calculate_price()
                            totalv = product.calculate_total()
                            para = ",".join([
                                product.id, 
                                product.name, 
                                product.category, 
                                str(product.price), 
                                str(product.stock), 
                                str(total), 
                                str(totalv)
                            ])
                            write_product(para)
                        except Exception as e:
                            logging.error(f"Error calculating totals for product {product.id}: {e}")
                else:
                    logging.warning(f"Line {line_number} malformed: {line.strip()}")
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
    except Exception as e:
        logging.error(f"Error loading products from {file_path}: {e}")
    return products



def write_order(order_data):
    try:
        with open('order_history.txt', 'a') as file:
            file.write(order_data + '\n')
    except Exception as e:
        logging.error(f"Error writing order to file: {e}")


def main():
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
        print(f"ID: {prod.id} | Name: {prod.name} | Category: {prod.category} | Price: {prod.price} | Stock: {prod.stock}")

    order_id = input("\nEnter the product ID to order: ").strip()
    selected_product = next((p for p in products if p.id == order_id), None)

    if selected_product:
        quantity = int(input(f"Enter quantity to order (Available: {selected_product.stock}): "))
        if quantity > selected_product.stock:
            print("Not enough stock available.")
            logging.warning(f"User {user.name} tried to order {quantity} of {selected_product.id} but only {selected_product.stock} available.")
            return

        total_price = selected_product.price * quantity
        if isinstance(selected_product, mx.Electronics):
            total_price += 0.15 * total_price
        elif isinstance(selected_product, mx.Clothing):
            total_price -= 0.10 * total_price

        selected_product.stock -= quantity

        order_data = f"{user.name},{user.email},{selected_product.id},{selected_product.name},{quantity},{total_price:.2f}"
        write_order(order_data)

        print(f"Order placed successfully! Total price: ${total_price:.2f}")
        logging.info(f"Order placed: {order_data}")
    else:
        print("Product ID not found.")
        logging.warning(f"User {user.name} tried to order invalid product ID: {order_id}")


if __name__ == "__main__":
    main()