from flask import Flask, jsonify
import psycopg2
from psycopg2 import sql
from psycopg2 import OperationalError

app = Flask(__name__)

def get_db_connection():
    try:
        conn = psycopg2.connect(
            dbname="microapp",   # Your database name
            user="myuser",     # Your PostgreSQL username
            password="mypassword",  # Your PostgreSQL password
            host="localhost",    # PostgreSQL host (change this if you're using Docker/Kubernetes)
            port="5432"          # Default PostgreSQL port
        )
        return conn
    except OperationalError as e:
        print(f"Error connecting to database: {e}")
        return None

# Example usage:
connection = get_db_connection()
if connection:
    print("Connected to the database")
    # Perform your queries here
    connection.close()
else:
    print("Failed to connect to the database")

@app.route('/')
def home():
    return 'Hello from Flask Backend!'

@app.route('/products')
def get_products():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM products')
    products = cur.fetchall()
    cur.close()
    conn.close()
    
    # Return data as JSON
    return jsonify(products)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
