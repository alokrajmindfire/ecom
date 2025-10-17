
# 🛒 Product Processing and Ordering System

A **multithreaded, CLI-based Python application** that processes product data, performs safe concurrent file operations, and allows users to place product orders — with robust logging and error handling throughout.

---

## 📋 Features

* 🧵 **Multithreaded product loading** — processes multiple products concurrently for better performance
* 🔒 **Thread-safe file handling** — uses locks to safely read and write data
* 🧱 **Category-based product creation** — dynamically creates `Electronics`, `Clothing`, or `Product` instances
* 🧾 **Comprehensive logging** — captures all actions, warnings, and errors in `app.log`
* 💰 **Order management** — allows users to place and record orders via a simple CLI interface

---

## 🧠 Concepts Used

* Multithreading and synchronization using `threading.Lock()`
* Object-Oriented Design (Inheritance and Composition)
* Structured exception handling and logging
* CLI-based interactive user input/output
* File I/O with safe concurrent access

---

## 🧩 Project Structure

```
├── main.py                # Main program (product processing and ordering)
├── models.py              # Contains Product, Electronics, Clothing, and User classes
├── products.txt           # Input file with product data
├── final.txt              # Output file storing processed products
├── order_history.txt      # File storing order history
├── app.log                # Application log file
└── README.md              # Project documentation
```

---

## ⚙️ Setup & Installation

### 1️⃣ Requirements

* **Python 3.8+**
* No external libraries required (uses Python standard library)

### 2️⃣ Clone the Repository

```bash
git clone https://github.com/alokrajmindfire/ecom.git
cd product-ordering-system
```

---

## 📦 Input File Format

Create a file named `products.txt` in the same folder with this format:

```
P001,Smartphone,Electronics,499.99,10
P002,Jeans,Clothing,39.99,25
P003,Notebook,Stationery,12.50,100
P004,Laptop,Electronics,899.99,5
```

Each line = one product
**Format:** `ProductID,Name,Category,Price,Stock`

---

## ▶️ Run the Application

Run this command in your terminal:

```bash
python main.py
```

Then follow the on-screen instructions:

```
Enter product file name: products.txt

Available Products:
ID: P001 | Name: Smartphone | Category: Electronics | Price: 499.99 | Stock: 10
ID: P002 | Name: Jeans | Category: Clothing | Price: 39.99 | Stock: 25

Enter your name: Alok
Enter your email: alok@example.com
Enter the product ID to order: P002
Enter quantity to order (Available: 25): 2

Order placed successfully! Total price: $71.98
```

---

## 📁 Output Files

| File                    | Description                                  |
| ----------------------- | -------------------------------------------- |
| **`final.txt`**         | Stores processed product data (with totals). |
| **`order_history.txt`** | Stores user order details.                   |
| **`app.log`**           | Logs info, warnings, and errors.             |

---

## 🧾 Example Log Output

```
2025-10-17 12:40:11 - INFO - Order placed: Alok,alok@example.com,P002,Jeans,2,71.98
2025-10-17 12:41:03 - ERROR - File not found: missing_products.txt
```

---

## 🧱 Error Handling

The system uses **specific exception handling** for clarity:

* `ValueError`, `TypeError` → Data conversion issues
* `OSError`, `IOError` → File read/write issues
* `RuntimeError` → Threading issues

Unexpected exceptions are logged without crashing the program.

---

## 🚀 Future Enhancements

* Add database integration (SQLite/PostgreSQL)
* Add async file handling with `asyncio`
* Implement unit tests (`unittest` or `pytest`)
* Develop a web interface (Flask / FastAPI)

---