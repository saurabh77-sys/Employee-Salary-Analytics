from mysql.connector import connect
from getpass import getpass

conn = connect(
    host="127.0.0.1",
    user="root",
    password=getpass("Enter MySQL password:"),
    database="empolyee",
    port=3306,
    use_pure=True
)

cursor = conn.cursor()
print("-"*100)
print("TASK 1")

cursor.execute("SELECT * FROM employee_db")
data = cursor.fetchall()



for row in data:
  emp_name =row[1]
  salary =row[3]

  if salary>=50000:
    category = "High Salary"

  elif salary>=40000:
    category = "Medium Salary"

  else:
    category = "Low Salary" 

  print(emp_name,("~"),salary,("~"),category)  
print("-"*100)
print("TASK 2")



for row in data:
    emp_name = row[1]
    salary = row[3]
    department = row[2]
    if department == "IT":
      bonus_percent = 0.15
    elif department =="Sales":
      bonus_percent = 0.10
    else :
      bonus_percent = 0.08 

    bonus = salary * bonus_percent  
    final_salary = salary + bonus
    print(emp_name,("~"), bonus,("~"),final_salary)
print("-"*100) 
print("TASK 3")
 

cursor.execute(" select * from employee_db where salary >40000")
data = cursor.fetchall()
for row in data:
  salary = row[3]
  emp_name = row[1]
  if salary >= 50000:
    tax = 0.10 
  else :
    tax = 0.05

  tax_amount = salary*tax
  salary_aftertax = salary - tax_amount

  print(emp_name,("~"),salary,("~"),tax,("~"),tax_amount,("~"),salary_aftertax)

print("-"*100)  

print("TASK 4")


cursor.execute("select * from employee_db")
data = cursor.fetchall()
for row in data:
  department = row[2]
  salary = row[3]
  emp_name = row[1]
  if department=="IT":
    score =90 
  elif department == "Sales":
    score =80
  else :
    score = 75

  if score >=90:
      bonus = 0.15
  elif score >= 80:
      bonus = 0.10
  else :
      bonus = 0.05

  bonus_amount =salary * bonus

  print(emp_name,("~"),department,("~"),score,("~"),bonus_amount)
print("-"*100)  
print("TASK 5")



#cursor.execute("""create table employee_summary (emp_id int ,emp_name varchar(45), department varchar(45),salary float,bonus float , final_salary int)""")
cursor.execute("select * from employee_db")
data = cursor.fetchall()

for row in data :
  salary = row [3]
  if salary>=50000:
    bonus = 0.10
  else :
     bonus = 0.05

  bonus_amount = salary*bonus 
  final_salary = salary+bonus_amount

  emp_id = row[0]
  emp_name = row[1]
  department = row[2]

  cursor.execute("""
  insert into employee_summary
  (emp_id,emp_name,department,salary,bonus,final_salary) 
  values (%s,%s,%s,%s,%s,%s)""",
  (emp_id, emp_name, department, salary, bonus_amount, final_salary) )

conn.commit()

print("-"*100) 
print("TASK 6")


cursor.execute("select * from employee_db")
data = cursor.fetchall()

it_total = 0
hr_total = 0
sales_total = 0

it_count = 0
hr_count = 0
sales_count = 0

for row in data:
    department = row[2]
    salary = row[3]

    if department == "IT":
        it_total = it_total + salary
        it_count = it_count + 1

    elif department == "HR":
        hr_total = hr_total + salary
        hr_count = hr_count + 1

    else:
        sales_total = sales_total + salary
        sales_count = sales_count + 1

print("IT Total =", it_total)
print("HR Total =", hr_total)
print("Sales Total =", sales_total)

print("*-*" * 20)

it_avg = it_total / it_count
hr_avg = hr_total / hr_count
sales_avg = sales_total / sales_count

print("IT Average =", it_avg)
print("HR Average =", hr_avg)
print("Sales Average =", sales_avg)

print("-"*100) 
print("TASK 7")


cursor.execute("select * from employee_db")
data = cursor.fetchall()

for row in data:
  emp_name = row[1]
  salary = row[3]
  if salary>= 50000:
    status="Eligible for Promotion"
  else :
    status ="Not Eligible"
  print(emp_name,("~"),salary,("~"),status)

print("-" * 100)
print("TASK 8")

cursor.execute("SELECT * FROM employee_db")
data = cursor.fetchall()

for row in data:
    department = row[2]
    salary = row[3]
    emp_name = row[1]

    if department == "IT":
        incri = 0.12
    elif department == "Sales":
        incri = 0.10
    else:
        incri = 0.08

    incri_amount = salary * incri
    Incremented_Salary = salary + incri_amount

    print(emp_name, "~", salary, "~", Incremented_Salary)

    cursor.execute(
        """
        UPDATE employee_db
        SET salary = %s
        WHERE emp_id = %s
        """,
        (Incremented_Salary, row[0])
    )

conn.commit()

print("-"*100) 
print("TASK 9")

#cursor.execute(""" create table employee_eincentive(emp_id int ,emp_name varchar(45),department varchar(45),incentive int)""")

cursor.execute("select * from employee_db")
data = cursor.fetchall()

for row in data :
  emp_id = row[0]
  emp_name = row[1]
  department = row[2]
  salary= row[3]

  if salary>= 50000:
    incen = 5000
  elif salary>= 40000:
    incen = 3000
  else:
    incen = 2000  

  cursor.execute("""
    insert into employee_incentive
    (emp_id, emp_name , department , incentive)
    values (%s,%s,%s,%s)
    """,(emp_id,emp_name,department,incen))

conn.commit()


print("-"*100) 
print("TASK 10")

cursor.execute("select * from employee_db")
data = cursor.fetchall()
highest_salary = data [0][3]
lowest_salary = data[0][3]

for row in data :
  salary = row [3]

  if salary > highest_salary: 
    highest_salary = salary

  if salary < lowest_salary:
    lowest_salary = salary 

difference = highest_salary - lowest_salary


print("Highest Salary =",highest_salary)
print("Lowest Salary=",lowest_salary)
print("diffrence=",difference)
