create database test;

use test;

CREATE TABLE customer (
 customer_id INT unique not null PRIMARY KEY,
 customer_name VARCHAR(50) NOT NULL,
 category_id int NOT NULL,
 customer_phone varchar(50)
);

CREATE TABLE customerFinance (
 finance_account INT unique not null PRIMARY KEY,
 customer_id int not null,
 bank_id int not null,
 account_value int not null,
 start_date datetime,
 finish_date datetime
);

CREATE TABLE bank (
 bank_id INT unique not null PRIMARY KEY,
 bank_name varchar(50)
);

CREATE TABLE orders (
 order_id INT unique not null PRIMARY KEY,
 customer_id int not null,
 order_date datetime not null,
 order_state_id int not null,
 product_id int not null
);

CREATE TABLE product (
 product INT unique not null PRIMARY KEY,
 suplier_id int not null,
 product_name char(50),
 product_quantity int not null,
 product_price int not null
);

CREATE TABLE product (
 product_id INT unique not null PRIMARY KEY,
 suplier_id int not null,
 product_name char(50),
 product_quantity int not null,
 product_price int not null
);

CREATE TABLE warehousetask (
 task_id INT unique not null PRIMARY KEY,
 status_id int not null,
 order_id int not null,
 product_id int not null,
 worker_id int not null,
 date_time_started datetime not null,
 date_time_finished datetime
);

CREATE TABLE warehouseworker (
 worker_id INT unique not null PRIMARY KEY,
 task_id int,
 position_id int not null,
 worker_name char(50),
 worker_start_date date not null,
 pallet_id int unique
);

CREATE TABLE workerposition (
 position_id INT unique not null PRIMARY KEY,
 position_type varchar(50),
 prosition_salary int not null
);

CREATE TABLE pallet (
 pallet_id INT unique not null PRIMARY KEY,
 worker_id int,
 pallet_status_id int not null,
 pallet_product_id int,
 product_quantity int
);

CREATE TABLE taskstatus (
 status_id INT unique not null PRIMARY KEY,
 task_type varchar(50)
);

CREATE TABLE supplier (
 supplier_id INT unique not null PRIMARY KEY,
 supplier_name char(50),
 supplier_phone char(50)
);

CREATE TABLE supplierorder (
 order_id INT unique not null PRIMARY KEY,
 supplier_id int not null,
 product_id int not null,
 order_status_id int not null,
 start_date date not null,
 complete date date
);









LOAD DATA INFILE "table data//customer.csv"
INTO TABLE customer
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

select * from customer;

SHOW VARIABLES LIKE 'secure_file_priv'