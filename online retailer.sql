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

insert into bank (bank_id, bank_name) 
values (1, 'CBA'), (2, 'Westpac'), (3, 'St George');


CREATE TABLE orders (
 order_id INT unique not null PRIMARY KEY,
 customer_id int not null,
 order_date datetime not null,
 order_state_id int not null,
 product_id int not null
);

CREATE TABLE product (
 product_id INT unique not null PRIMARY KEY,
 supplier_id int not null,
 product_name char(50),
 product_quantity int not null,
 product_price int not null
);

select customer.customer_id, customer.customer_name, orders.order_date, product.product_name
from customer 
left join orders on customer.customer_id = orders.customer_id 
left join product on orders.product_id = product.product_id;



insert into product (product_id, supplier_id, product_name, product_quantity, product_price) 
values (1, 1, "basketball shoes", 50, 300), 
(2, 1, "running shoes", 200, 150), 
(3, 1, "football shoes", 250, 250),
(4, 1, "ballet shoes", 50, 400),
(5, 2, "twighlight", 100, 50),
(6, 2, "hobbit", 75, 25),
(7, 2, "senior school maths", 74, 35),
(8, 2, "poetry", 5, 25),
(9, 3, "shovel", 55, 45),
(10, 3, "potting mix", 40, 30),
(11, 3, "garden gnome", 10, 5);



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

insert into warehouseworker (worker_id, position_id, worker_name, worker_start_date) 
values (1, 1, "gary smith", '2018-11-01'), 
(2, 1, "albert kevin", '2020-06-20'), 
(3, 1, "frank marriot", '2018-06-01'), 
(4, 1, "kevin gandhi", '2018-01-01'), 
(5, 2, "Mr burns", '2017-11-01');

CREATE TABLE workerposition (
 position_id INT unique not null PRIMARY KEY,
 position_type varchar(50),
 position_salary int not null
);

insert into workerposition (position_id, position_type, position_salary) 
values (1, "basic worker", 50000),
(2, "manager", 75000); 

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


insert into taskstatus (status_id, task_type) 
values (1, 'inactive'), (2, 'started'), (3, 'finished');

CREATE TABLE supplier (
 supplier_id INT unique not null PRIMARY KEY,
 supplier_name char(50),
 supplier_phone char(50)
);

insert into supplier (supplier_id, supplier_name, supplier_phone) 
values (1, 'addidas', "01123434" ), 
(2, 'Book store', "4400055"), 
(3, 'garden store', "448858843");

CREATE TABLE supplierorder (
 order_id INT unique not null PRIMARY KEY,
 supplier_id int not null,
 product_id int not null,
 order_status_id int not null,
 start_date date not null,
 complete_date date
);

select host from information_schema.processlist;

select @@hostname;
show variables where Variable_name like '%host%';

select user();

CREATE USER 'gordon' IDENTIFIED BY "fjk54#djk^";
GRANT ALL PRIVILEGES ON test.* TO 'gordon';


LOAD DATa INFILE "table data//customer.csv"
INTO TABLE customer
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

select * from customer;

SHOW VARIABLES LIKE 'secure_file_priv'

show tables

SHOW GLOBAL VARIABLES LIKE 'local_infile';

SELECT CURRENT_USER();
SHOW GRANTS for 'gordon'

SET GLOBAL local_infile = 'ON';

SET GLOBAL local_infile=1;

define('DB_HOST', 'localhost')