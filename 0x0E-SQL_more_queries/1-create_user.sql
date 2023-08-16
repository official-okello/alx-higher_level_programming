-- Script that creates the MySQL server user user_0d_1

CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- flushes privileges after creating a user or granting a user permissions

FLUSH PRIVILEGES;

-- grants a user all permissions in root

GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
FLUSH PRIVILEGES;
