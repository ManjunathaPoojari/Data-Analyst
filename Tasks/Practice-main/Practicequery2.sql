
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(50),
    region VARCHAR(50)
);
INSERT INTO customers VALUES
(101, 'Alice', 'East'),
(102, 'Bob', 'West'),
(103, 'Charlie', 'North'),
(104, 'Dave', 'South');


CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    total_amount DECIMAL(10,2)
);
INSERT INTO orders VALUES
(1, 101, '2023-01-10', 500.00),
(2, 102, '2023-02-15', 300.00),
(3, 101, '2023-03-01', 700.00),
(4, 103, '2023-04-20', 450.00),
(5, 102, '2023-05-10', 200.00);


CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(50),
    category VARCHAR(50)
);
INSERT INTO products VALUES
(201, 'Laptop', 'Electronics'),
(202, 'Mouse', 'Accessories'),
(203, 'Headphones', 'Accessories');


CREATE TABLE order_details (
    detail_id INT PRIMARY KEY,
    order_id INT,
    product_id INT,
    quantity INT,
    unit_price DECIMAL(10,2)
);
INSERT INTO order_details VALUES
(1, 1, 201, 2, 200.00),
(2, 1, 202, 1, 100.00),
(3, 2, 203, 3, 100.00),
(4, 3, 201, 1, 700.00),
(5, 4, 202, 2, 225.00);

SELECT c.customer_id, c.customer_name, c.region, SUM(o.total_amount) AS customer_total
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.customer_name, c.region
HAVING SUM(o.total_amount) > (
    SELECT AVG(region_total)
    FROM (
        SELECT c2.region, SUM(o2.total_amount) AS region_total
        FROM customers c2
        JOIN orders o2 ON c2.customer_id = o2.customer_id
        GROUP BY c2.region
    ) AS regional_avg
);

SELECT od.order_id
FROM order_details od
JOIN products p ON od.product_id = p.product_id
GROUP BY od.order_id
HAVING COUNT(DISTINCT p.category) = (
    SELECT COUNT(DISTINCT category) FROM products
);

SELECT o.customer_id, c.customer_name, p.product_name, od.unit_price
FROM orders o
JOIN order_details od ON o.order_id = od.order_id
JOIN products p ON od.product_id = p.product_id
JOIN customers c ON o.customer_id = c.customer_id
WHERE o.order_date > '2023-01-01'
AND (o.customer_id, od.unit_price) IN (
    SELECT o2.customer_id, MAX(od2.unit_price)
    FROM orders o2
    JOIN order_details od2 ON o2.order_id = od2.order_id
    WHERE o2.order_date > '2023-01-01'
    GROUP BY o2.customer_id
);

SELECT DISTINCT region
FROM customers
WHERE customer_id NOT IN (
    SELECT o.customer_id
    FROM orders o
    JOIN order_details od ON o.order_id = od.order_id
    WHERE od.product_id = 203
);


