create database onlineretailer;

use onlineretailer;

CREATE TABLE customer (
 customer_id INT unique not null PRIMARY KEY AUTO_INCREMENT,
 customer_name VARCHAR(50) NOT NULL,
 category_id int default 1,
 customer_phone varchar(50)
);

CREATE TABLE customerFinance (
 finance_account INT unique not null,
 customer_id int not null,
 bank_id int not null,
 account_value int not null,
 start_date datetime,
 finish_date datetime,
 Primary Key (finance_account),
 Foreign Key (customer_id) references customer(customer_id)
);

CREATE TABLE bank (
 bank_id INT unique not null PRIMARY KEY,
 bank_name varchar(50)
);

CREATE TABLE supplier (
 supplier_id INT unique not null PRIMARY KEY,
 supplier_name char(50),
 supplier_phone char(50)
);

insert into supplier (supplier_id, supplier_name, supplier_phone) 
values (1, 'addidas', "01123434" ), 
(2, 'Book store', "4400055"), 
(3, 'garden store', "448858843");

CREATE TABLE product (
 product_id INT unique not null AUTO_INCREMENT,
 supplier_id int not null,
 product_name char(50),
 product_quantity int not null,
 product_price int not null,
 Primary Key (product_id),
 Foreign Key (supplier_id) references supplier(supplier_id)
);

create table states(
state_id int unique not null,
statetype VARCHAR(50) NOT NULL,
primary key (state_id)
);

Create Table currentstate(
current_state_id int unique Not Null auto_increment,
state_id int not null,
statedate datetime not null,
Primary Key (current_state_id),
foreign Key(state_id) references states(state_id)
);

CREATE TABLE orders (
 order_id INT not null,
 customer_id int not null,
 current_state_id int NOT NULL,
 Primary Key (order_id),
 Foreign Key (customer_id) references customer(customer_id),
 Foreign Key (current_state_id) references currentstate (current_state_id)
);

CREATE TABLE orderproducts(
id int not null,
order_id int not null,
product_id int not null,
quantity int not null,
current_state_id int not null,
primary key (id),
Foreign Key (order_id) references orders(order_id),
 Foreign Key (product_id) references product(product_id),
 Foreign Key (current_state_id) references currentstate (current_state_id)
);

CREATE TABLE workerposition (
 position_id INT unique not null Primary Key,
 position_type varchar(50),
 position_salary int not null
);


CREATE TABLE warehouseworker (
 worker_id INT unique not null AUTO_INCREMENT,
 position_id int not null,
 worker_name char(50),
 worker_start_date date not null,
 order_id int,
 pallet_id int,
 Primary Key (worker_id),
 Foreign Key(order_id) references orders(order_id),
 Foreign Key(position_id) references workerposition(position_id)
);

CREATE TABLE supplierorder (
 order_id INT not null,
 supplier_id int not null,
 product_id int not null,
 quantity int not null,
 current_state_id int not null,
 Primary Key (order_id),
 foreign key (supplier_id) references supplier(supplier_id),
 foreign key (product_id) references product(product_id),
 foreign key (current_state_id) references currentstate(current_state_id)
);


insert into states(state_id, statetype) 
values(1, 'order placed'),
(2, 'order currently being picked'),
(3, 'order shipped'),
(4, 'inactive'),
(5, 'currently picking');

insert into workerposition (position_id, position_type, position_salary) 
values (1, "basic worker", 50000),
(2, "manager", 75000);

/* 

#create customer
insert into customer (customer_name, category_id, customer_phone) values ("steve", 1, "55533");

insert into supplier (supplier_id, supplier_name, supplier_phone) 
values (1, 'addidas', "01123434" ), 
(2, 'Book store', "4400055"), 
(3, 'garden store', "448858843");

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

#create worker
insert into warehouseworker (position_id, worker_name, worker_start_date) 
values (1, "gary smith", '2018-11-01'), 
(1, "albert kevin", '2020-06-20'), 
(1, "frank marriot", '2018-06-01'), 
(1, "kevin gandhi", '2018-01-01'), 
(2, "Mr burns", '2017-11-01');

insert into bank (bank_id, bank_name) 
values (1, 'CBA'), (2, 'Westpac'), (3, 'St George');



#add order
insert into orders
value(1, 1, 1, 1, 3);

#update order state
insert into currentstate(state_id, statedate)
values("relevant id", "relevant date");

SELECT current_state_id FROM currentstate ORDER BY current_state_id DESC LIMIT 1;

update orders
set current_state_id = "X"
where orders.order_id = "y";

#get products table
select distinct product_name from product;

#update products table
update product
set product_quantity = "x"
where product_id = "y";

update product
set product_price = "x"
where product_id = "y";

#get sum of products ordered
select product.product_name, sum(product.product_id) as quantity,  sum(product.product_id)* product.product_price as totalsales
from product inner join orders on product.product_id = orders.product_id
where orders.current_state_id = 1
group by product.product_id;

#update worker pallet
update warehouseworker
set pallet_id = "x"
where worker_id = "y";

#get customer orders and their status's
select customer.customer_id, customer.customer_name, product.product_name, orders.quantity, states.statetype
from customer inner join orders on customer.id = orders.customer_id
left join products on orders.product_id = product.product_id
left join currentstate on orders.current_state_id = currentstate.current_state_id
left join states on currentstate.current_state_id = states.state_id;

#create pallet
insert into pallet(worker_id, order_id, pallet_state_id, pallet_product_id, product_quantity)
values(1,1,1,1,3);

#update pallet status
insert into currentstate(state_id, statedate)
values("relevant id", "relevant date");

SELECT current_state_id FROM currentstate ORDER BY current_state_id DESC LIMIT 1;

update pallet
set pallet_state_id = "x"
where pallet_id = "y";

insert into supplierorder(order_id, supplier_id, product_id, quantity, current_state_id)
values(1, 1, 1, 1,40, 3);
*/
