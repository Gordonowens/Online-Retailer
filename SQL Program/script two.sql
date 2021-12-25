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
 order_id INT not null auto_increment,
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