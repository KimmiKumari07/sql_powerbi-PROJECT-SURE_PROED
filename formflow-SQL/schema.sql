CREATE DATABASE IF NOT EXISTS formflow_db;
USE formflow_db;

CREATE TABLE IF NOT EXISTS responses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100),
    email VARCHAR(100),
    phone VARCHAR(20),
    course VARCHAR(100),
    feedback TEXT,
    timestamp DATETIME,
    UNIQUE (timestamp)
);