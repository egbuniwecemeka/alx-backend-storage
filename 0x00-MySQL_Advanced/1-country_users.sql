-- MySQL script that creates a table
    -- id: integer, never null, auto increment, primary key
    -- email: string (255 characters), never null, unique
    -- name: string (255 characters),
    -- country: enumeration (US, CO, TN), never null, default is US

CREATE TABLE IF NOT EXISTS `users` (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US'
);
