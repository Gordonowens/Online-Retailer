import mysql.connector
import pandas

mydb = mysql.connector.connect(
  host="DESKTOP-S5B5DOL",
  user="gordon",
  password="xxxx",
   
  db = "test"
)


mycursor = mydb.cursor()

#mycursor.execute("CREATE TABLE customerFinance(finance_account INT unique not null PRIMARY KEY,customer_id int not null,bank_id int not null,account_value int not null,start_date datetime,finish_date datetime);")

#mycursor.execute('LOAD DATA LOCAL INFILE "C://Users//User//Documents//online retailer//table data//customer.csv" ' + "INTO TABLE customer FIELDS TERMINATED BY ','  ENCLOSED BY " + "'" + '"' + "' LINES TERMINATED BY '\n' IGNORE 1 ROWS;")


#mycursor.execute("insert into taskstatus (status_id, task_type) values (1, 'inactive'), (2, 'started'), (3, 'finished');")

#create customer and make order
mycursor.execute("insert into customer (customer_id, customer_name, category_id, customer_phone)\
                 values (1, 'john smith', 5, '04005500');")

mycursor.execute("insert into orders (order_id, customer_id, order_date, order_state_id, product_id)\
                 values (1, 1, '2018-01-01', 1, 3);")

mycursor.execute("select customer.customer_id, customer.customer_name, orders.order_date, product.product_name from customer left join orders on customer.customer_id = orders.customer_id left join product on orders.product_id = product.product_id;")



myresult = mycursor.fetchall()
print(myresult)

