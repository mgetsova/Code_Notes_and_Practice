/*
look at this dude's leetcode SQL repo on GitHub:
https://github.com/itsyagirlLavender007/leetcode-SQL/blob/main/14-confirmation-rate.sql
*/

/*
Learn SQL tutorial notes:
*/

/* below selects all columns from table titled car, ; ends the command */
SELECT *
FROM car;

/* below selects model and price columns only from table car */
SELECT model, price FROM car;

/* below selects all columns from car where production_year = 1999 */
SELECT * 
FROM car
WHERE production_year = 1999;

/* can also do: */
SELECT * FROM car WHERE price > 10000;
/* or with other conditional operators, 
 > < >= <= 
 there is also <> or != for not equal 
 and LIKE for string comparison */
SELECT * FROM items_ordered
WHERE item LIKE 'Tent';

/* so ended the supposedly free tutorial */

/* free code camp has a 4 hour youtube video on SQL which may be the only
resource on the entire internet, there are no SQL walk throughs for free. */

/* DISTINCT keyword will return all the unqiue ages in the specified column */
SELECT DISTINCT age FROM employee_info;
/* ALL will display all of the specifide columns including duplicates, this is
the default if nothing else is specified */


/* Select the customerid, order_date, and item values from the items_ordered table for any items in the item column that start with the letter “S”. */
SELECT customerid, order_date, item
FROM items_ordered
WHERE item LIKE 's%';
/* Select the distinct items in the items_ordered table. In other words, display a listing of each of the unique items from the items_ordered table. */
SELECT DISTINCT item
FROM items_ordered;

/*
AGGREGATE FUNCTIONS
MIN = smallest value in given column
MAX = largest val in given col
SUM = sum of numeric values in given col
AVG = avg val of given col
COUNT = total number of vals in a given col
COUNT(*) = number of rows in a table


average salary in whole employee table: */
SELECT AVG(salary) FROM employee;

/* average salary of programmer employees only: */
SELECT AVG(salary) FROM employee WHERE title = 'Programmer';


/* 
GROUP BY
gather all the rows together that contain data in the specified column(s)
allows aggregate functions to be performed on one or more columns

ex: retrieve a list of the highest paid salaries in each dept: */
SELECT MAX(salary), dept FROM employee GROUP BY dept;
/* above will display the salary for the person that makes the most in each dept */


/* How many people are in each unique state in the customers table? Select the state and display the number of people in each. */
SELECT state, count(state)
FROM customers
GROUP BY state;

/* From the items_ordered table, select the item, maximum price, and minimum price for each specific item in the table. */
SELECT item, max(price), min(price)
FROM items_ordered
GROUP BY item;

/* How many orders did each customer make? */
SELECT customerid, count(customerid), sum(price)
FROM items_ordered
GROUP BY customerid;

/* 
HAVING
Let’s say you have an employee table containing the employee’s name, 
department, salary, and age. You want to select the avg salalry for each
employee in each department only if their salalry is over 20000 */
SELECT dept, avg(salary)
FROM employee
GROUP BY dept
HAVING avg(salary) > 20000;

/* How many people are in each unique state in the customers table that have more than one person in the state? */
SELECT state, count(state) 
FROM customers 
GROUP BY state 
HAVING count(state) > 1;

/* From the items_ordered table, select the item, maximum price, and minimum price for each specific item in the table. Only display the results if the maximum price for one of the items is greater than 190.00. */
SELECT item, MAX(price), MIN(price)
FROM items_ordered
GROUP BY item
HAVING MAX(price) > 190.00;

/* How many orders did each customer make? Use the items_ordered table. Select the customerid, number of orders they made, and the sum of their orders if they purchased more than 1 item. */
SELECT customerid, COUNT(customerid), SUM(price)
FROM items_ordered
GROUP BY customerid
HAVING COUNT(customerid) > 1;


/*
ORDER BY
display results of query in sorted order based on specified columns, with 
default ordering being ascending (ASC), can change to descending (DESC)*/
SELECT employee_id, dept, name, age, salary 
FROM employee_info 
WHERE dept = 'Sales' 
ORDER BY salary;

/* can also order by multiple columns */
SELECT employee_id, dept, name, age, salary 
FROM employee_info 
WHERE dept = 'Sales' 
ORDER BY salary, age DESC;

/* Select the lastname, firstname, and city for all customers in the customers table. Display the results in Ascending Order based on the lastname. */
SELECT lastname, firstname, city
FROM customers
ORDER BY lastname;

/* Same thing as exercise #1, but display the results in Descending order. */
SELECT lastname, firstname, city
FROM customers
ORDER BY lastname DESC;

/* Select the item and price for all of the items in the items_ordered table that the price is greater than 10.00. Display the results in Ascending order based on the price. */
SELECT item, price
FROM items_ordered
WHERE price > 10.00
ORDER BY price; /* or ORDER BY price ASC; */

/* COMBINING CONDITIONS & BOOLEAN OPERATORS
AND and OR operators can be used to join two or more conditions in the WHERE clause
can use parenthesis around conditional expressions to make easier to read but not required
*/

/* Select the customerid, order_date, and item from the items_ordered table for all items unless they are ‘Snow Shoes’ or if they are ‘Ear Muffs’. */
SELECT customerid, order_date, item
FROM items_ordered
WHERE item <> 'Snow Shoes' AND item <> 'Ear Muffs';

/* Select the item and price of all items that start with the letters ‘S’, ‘P’, or ‘F’. */
SELECT item, price
FROM items_ordered
WHERE item LIKE 'S%' OR item LIKE 'P%' OR item LIKE 'F%';

/* IN AND BETWEEN 
The IN conditional operator is really a set membership test operator. 
That is, it is used to test whether or not a value (stated before the 
keyword IN) is “in” the list of values provided after the keyword IN.
*/
SELECT employeeid, lastname, salary
FROM employee_info
WHERE lastname IN ('Hernandez', 'Jones', 'Roberts', 'Ruiz');
/* can also use NOT IN 

The BETWEEN conditional operator is used to test to see whether or not a 
value (stated before the keyword BETWEEN) is “between” the two values stated
after the keyword BETWEEN.
*/
SELECT employeeid, age, lastname, salary 
FROM employee_info 
WHERE age BETWEEN 30 AND 40;
/* can also use NOT BETWEEN */

/* MATHEMATICAL FUNCTIONS
+ addition
- subtraction
* multiplication 
/ division
% modulo

ABS(x) absolute val of x
SIGN(x) returns signs of input x as -1, 0, 1 (negative, zero, positive)
MOD(x, y) same as x%y
FLOOR(x) largest int val that is <= x
CEILING(x) or CEIL(x) smallest int val that is >= x
POWER(x, y) x^y
ROUND(x) x rounded to nearest whole int
ROUND(x, d) x rounded to d decimal places
SQRT(x) square root of x


Select the item and per unit price for each item in the items_ordered table. Hint: Divide the price by the quantity. */
SELECT item, SUM(price) / SUM(quantity)
FROM items_ordered
GROUP BY item;

/* TABLE JOINS
"Join" makes relational databases relational
allows you to link data between 2 or more tables into a single query result
from one single select statement 

Join can be recognized in a SQL SELECT statement if it has more than one table
after the FROM keyword

say you have a "Customer_info" table and a "Purchases" table
they have a common "customer_number" column which can be used to join the two tables
let's say you want to select the customer's name and the items they've purchased 

known as an "Inner Join" or "Equijoin"
*/
SELECT customer_info.firstname, customer_info.lastname, purchases.item 
FROM customer_info, purchases 
WHERE customer_info.customer_number = purchases.customer_number;
/* some databases may not take the above, an alternative is : */
SELECT customer_info.firstname, customer_info.lastname, purchases.item 
FROM customer_info INNER JOIN purchases 
ON customer_info.customer_number = purchases.customer_number;

/* Write a query using a join to determine which items were ordered by each of the customers in the customers table. Select the customerid, firstname, lastname, order_date, item, and price for everything each customer purchased in the items_ordered table. */
SELECT customers.customerid, items_ordered.order_date, items_ordered.item, items_ordered.price, customers.firstname, customers.lastname
FROM customers, items_ordered
WHERE customers.customerid = items_ordered.customerid;

/* Repeat the above, however display the results sorted by state in descending order. */
SELECT customers.customerid, items_ordered.order_date, items_ordered.item, items_ordered.price, customers.firstname, customers.lastname
FROM customers, items_ordered
WHERE customers.customerid = items_ordered.customerid
ORDER BY customers.state DESC;