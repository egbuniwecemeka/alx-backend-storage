# 0x00. MySQL advanced

SE Foundations Revision

## Updates and Installation

[Link](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-20-04#step-2-configuring-mysql)

STEP 1 Update package and Dependencies
    - sudo apt update
    - sudo apt update -y
    - sudo apt install mysql-server -y

STEP 2. Install MySQL
    - sudo apt install mysql-server -y
    __To connect to a remote MySQL server only, install only MySQL Client__
    - sudo apt install mysql-client
    - mysql --version

STEP 3. Securing MySQL
    - sudo mysql_secure_installation (validates password components). There are 3 levels. 0 - Low, 1 - Medium, 2 - Strong

STEP 4. Check MySQL service status
    sudo systemctl status mysql
    sudo systemctl start mysql.service

STEP 5. Log in to MySQL Server
    sudo mysql -u root