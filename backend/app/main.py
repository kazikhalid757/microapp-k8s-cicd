from flask import Flask, jsonify
import psycopg2
from psycopg2 import OperationalError

app = Flask(__name__)

# Database connection config
DB_CONFIG = {
    "dbname": "microapp",
    "user": "myuser",
    "password": "mypassword",
    "host": "postgres",  # Service name from Kubernetes
    "port": "5432"
}

def get_db_connection():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        return conn
    except OperationalError as e:
        print(f"Error connecting to database: {e}")
        return None

@app.route('/')
def home():
    return 'Hello from Flask Backend!'

@app.route('/test')
def test():
    return 'Test API End point!'

@app.route('/db-connection')
def db_connection():
    conn = get_db_connection()
    if conn:
        conn.close()
        return jsonify({"status": "success", "message": "Connected to database"})
    else:
        return jsonify({"status": "fail", "message": "Failed to connect to database"}), 500

@app.route('/products')
def get_products():
    conn = get_db_connection()
    if conn is None:
        return jsonify({"error": "Database connection failed"}), 500

    try:
        cur = conn.cursor()
        cur.execute('SELECT id, name, price, created_at FROM products')
        rows = cur.fetchall()
        products = [
            {"id": row[0], "name": row[1], "price": float(row[2]), "created_at": row[3].isoformat()}
            for row in rows
        ]
        cur.close()
        conn.close()
        return jsonify(products)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
