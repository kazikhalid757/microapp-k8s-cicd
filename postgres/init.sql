-- Create a new database
CREATE DATABASE microapp;

-- Connect to the new database
\c microapp;

-- Create a new table (for example, products)
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    price NUMERIC(10, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert some sample data
INSERT INTO products (name, price) VALUES
('Laptop', 1200.00),
('Smartphone', 800.00),
('Keyboard', 40.00);

-- Create a user (optional, if needed)
-- CREATE USER microapp_user WITH ENCRYPTED PASSWORD 'password123';
-- GRANT ALL PRIVILEGES ON DATABASE microapp TO microapp_user;
