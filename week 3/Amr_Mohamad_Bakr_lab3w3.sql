-- ================ Task 1: Indexing and Performance =====================

CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    transaction_amount DECIMAL(10, 2),
    transaction_date TIMESTAMP
);

INSERT INTO transactions (transaction_amount, transaction_date)
SELECT ROUND(RANDOM() * 1000, 2), NOW() - INTERVAL '1 day' * (RANDOM() * 365)
FROM generate_series(1, 10000);

EXPLAIN ANALYZE 
SELECT * FROM transactions WHERE transaction_amount > 500;

CREATE INDEX idx_transaction_amount ON transactions (transaction_amount);

EXPLAIN ANALYZE 
SELECT * FROM transactions WHERE transaction_amount > 500;

-- =================== Task 2: Working with JSON Data ======================

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    details JSONB
);

INSERT INTO products (name, details) VALUES 
('Smartphone', '{"price": 500, "stock": 50, "tags": ["electronics", "sale"]}'),
('Laptop', '{"price": 1200, "stock": 20, "tags": ["electronics", "new"]}'),
('Book', '{"price": 20, "stock": 100, "tags": ["literature"]}');

SELECT name, details 
FROM products 
WHERE details -> 'tags' ? 'electronics';

-- ================= Task 3: Transactions and Error Handling ==============

CREATE TABLE inventory (
    product_id SERIAL PRIMARY KEY,
    stock INT,
    last_updated TIMESTAMP
);

BEGIN;

-- Update stock for a product
UPDATE inventory SET stock = 40 WHERE product_id = 1;

-- Insert invalid data (e.g., duplicate product_id)
INSERT INTO inventory (product_id, stock, last_updated)
VALUES (1, 100, NOW());

-- If error occurs, use rollback
ROLLBACK;
