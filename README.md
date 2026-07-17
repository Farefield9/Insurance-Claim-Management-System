# Insurance-Claim-Management-System

Create:
requirements.txt

Add:
mysql-connector-python
pandas
openpyxl

In CMD write:
pip install -r requirements.txt
after changing the directory to the directory where requirements.txt is saved

create:
db.py
change:
password="your_password" with your mysql password in db.py

Open MySQL and run:
CREATE DATABASE insurance_db;
USE insurance_db;

create tables:
CREATE TABLE users(
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50),
    password VARCHAR(50),
    role VARCHAR(20)
);

CREATE TABLE customers(
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    phone VARCHAR(15),
    email VARCHAR(100),
    address VARCHAR(200)
);

CREATE TABLE policies(
    policy_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    policy_type VARCHAR(50),
    premium DECIMAL(10,2),
    start_date DATE,
    end_date DATE,

    FOREIGN KEY(customer_id)
    REFERENCES customers(customer_id)
);

CREATE TABLE claims(
    claim_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    policy_id INT,
    claim_date DATE,
    claim_amount DECIMAL(10,2),
    reason VARCHAR(200),
    status VARCHAR(20),

    FOREIGN KEY(customer_id)
    REFERENCES customers(customer_id),

    FOREIGN KEY(policy_id)
    REFERENCES policies(policy_id)
);


INSERT INTO users(username,password,role)
VALUES
('admin','admin123','Admin');




create:
main.py

Run:
python main.py in cmd
Expected output:
Database Connected Successfully
System Ready


Create:
login.py

Create:
dashboard.py

Update main.py:
add import login at top 

Now run:
python main.py in cmd



Expected Result
You will see:

--------------------------------
Insurance Claim Management System

Username: ________

Password: ________

        LOGIN
--------------------------------


Enter:
Username:
admin

Password:
admin123

Then:
Login Successful

↓

Dashboard Opens

Welcome Admin

[Customer Management]
[Policy Management]
[Claim Management]
[Reports]


Create:
customer.py



Run:
python main.py in cmd

Login:
username: admin
password: admin123

Open:
Customer Management

Try adding:
Name:
Mannan

Phone:
9876543210

Email:
mannan@gmail.com

Address:
Delhi

Click:
Add Customer

You should see the customer appear in the table.

Also add this import at the top of dashboard.py:
import policy

Create:
policy.py


Run:
python main.py

Login:
Username: admin
Password: admin123

Open:
Policy Management

Example:
Customer ID:
1

Policy Type:
Health Insurance

Premium:
5000

Start Date:
2026-01-01

End Date:
2027-01-01

Click:
Add Policy

You should see:
Policy ID	Customer ID	Policy Type	Premium
1	1	Health Insurance	5000

Add import at top of dashboard.py:
import claims

Create:
claims.py

Run:
python main.py

Login:
admin
admin123

Open:
Claim Management

Example:
Customer ID:
1

Policy ID:
1

Claim Date:
2026-07-17

Claim Amount:
25000

Reason:
Hospital Expense

Click:
Submit Claim

It will appear:
Claim ID	Customer	Policy	Amount	Status
1	1	1	25000	Pending

Select it and click:
Approve

Status changes:
Approved

Add import at top of dashboard:
import reports

Create:
reports.py

Run:
python main.py

Login:
admin
admin123

Open:
Reports

Click:
Export Customer Report

You will get:
customers_report.csv

Example:
customer_id	name	phone
1	Mannan	9876543210

Open MySQL.
Run:
USE insurance_db;


CREATE VIEW claim_dashboard AS
SELECT
c.name AS Customer_Name,
p.policy_type AS Policy_Type,
cl.claim_date,
cl.claim_amount,
cl.status
FROM claims cl
JOIN customers c
ON cl.customer_id=c.customer_id
JOIN policies p
ON cl.policy_id=p.policy_id;

CREATE VIEW policy_dashboard AS
SELECT
policy_type,
COUNT(*) AS Total_Policies,
SUM(premium) AS Total_Premium
FROM policies
GROUP BY policy_type;

CREATE VIEW claim_status_dashboard AS
SELECT
status,
COUNT(*) AS Total_Claims,
SUM(claim_amount) AS Total_Amount
FROM claims
GROUP BY status;

