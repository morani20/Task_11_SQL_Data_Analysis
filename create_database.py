import sqlite3

def init_db():
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()

    # 1. Create products table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        product_id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_name TEXT NOT NULL,
        category TEXT NOT NULL,
        price REAL NOT NULL
    );
    ''')

    # Add 5 products if table is empty
    cursor.execute("SELECT COUNT(*) FROM products;")
    if cursor.fetchone()[0] == 0:
        products_data = [
            ('Laptop', 'Electronics', 1000.0),
            ('Smartphone', 'Electronics', 600.0),
            ('Wireless Headphones', 'Accessories', 80.0),
            ('Mechanical Keyboard', 'Accessories', 50.0),
            ('Gaming Monitor', 'Electronics', 300.0)
        ]
        cursor.executemany('''
        INSERT INTO products (product_name, category, price) 
        VALUES (?, ?, ?);
        ''', products_data)

    # 2. Create customers table (Step 1 requirement)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS customers (
        customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_name TEXT NOT NULL,
        city TEXT NOT NULL,
        signup_date DATE NOT NULL
    );
    ''')

    # Add 15 customers leaving the last 2 with zero purchases
    cursor.execute("SELECT COUNT(*) FROM customers;")
    if cursor.fetchone()[0] == 0:
        customers_data = [
            ('Ahmed Mahmoud', 'Gaza', '2023-01-15'),
            ('Sara Ali', 'Riyadh', '2023-02-10'),
            ('Mohamed Khaled', 'Jeddah', '2023-02-20'),
            ('Omar Farooq', 'Cairo', '2023-03-05'),
            ('Mona Hassan', 'Gaza', '2023-03-12'),
            ('Khaled Al-Abd', 'Riyadh', '2023-04-01'),
            ('Fatima Said', 'Dubai', '2023-04-15'),
            ('Youssef Ibrahim', 'Amman', '2023-05-01'),
            ('Rania Khalil', 'Gaza', '2023-05-20'),
            ('Hamza Sulaiman', 'Jeddah', '2023-06-04'),
            ('Laila Tariq', 'Cairo', '2023-06-18'),
            ('Belal Mustafa', 'Dubai', '2023-07-01'),
            ('Nada Youssef', 'Amman', '2023-07-15'),
            ('Abdullah Rami', 'Gaza', '2023-08-01'),  # Inactive customer (0 purchases)
            ('Heba Salama', 'Riyadh', '2023-08-10')    # Inactive customer (0 purchases)
        ]
        cursor.executemany('''
        INSERT INTO customers (customer_name, city, signup_date) 
        VALUES (?, ?, ?);
        ''', customers_data)

    # 3. Create sales table linked to product_id and customer_id
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS sales (
        sale_id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_id INTEGER REFERENCES products(product_id),
        quantity INTEGER NOT NULL,
        sale_date DATE NOT NULL,
        customer_id INTEGER REFERENCES customers(customer_id)
    );
    ''')

    # Distribute 30 sales transactions among the first 13 customers only
    cursor.execute("SELECT COUNT(*) FROM sales;")
    if cursor.fetchone()[0] == 0:
        customer_mapping = [
            1, 2, 3, 1, 4, 5, 2, 6, 7, 1, 
            8, 9, 3, 10, 2, 11, 12, 5, 13, 1, 
            4, 6, 7, 3, 8, 9, 10, 2, 11, 12
        ]
        
        sales_data = []
        for i in range(30):
            prod_id = (i % 5) + 1
            qty = (i % 3) + 1
            month = (i % 6) + 1
            sale_date = f"2023-0{month}-10"
            cust_id = customer_mapping[i]
            sales_data.append((prod_id, qty, sale_date, cust_id))
            
        cursor.executemany('''
        INSERT INTO sales (product_id, quantity, sale_date, customer_id) 
        VALUES (?, ?, ?, ?);
        ''', sales_data)

    conn.commit()
    conn.close()
    print("✓ Database store.db created, expanded, and populated successfully!")

if __name__ == '__main__':
    init_db()