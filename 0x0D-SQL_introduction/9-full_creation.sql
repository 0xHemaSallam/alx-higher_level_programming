/* Write a script that creates a table second_table in the database hbtn_0c_0 in your MySQL server and add multiples rows.

second_table description:
id INT
name VARCHAR(256)
score INT
The database name will be passed as an argument to the mysql command
If the table second_table already exists, your script should not fail
 */

 -- task 9

 CREATE Table IF NOT EXISTS second_table( id INT, name VARCHAR(256), score INT);
