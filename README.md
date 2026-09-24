# Employee Salary Analytics

A Python + MySQL project that runs 10 salary-analysis tasks over an employee database.

## What it does
Connects to a MySQL database (`empolyee`, table `employee_db`) and performs 10 tasks:

1. **Salary categorization** — labels each employee High (≥ ₹50,000), Medium (≥ ₹40,000), or Low salary.
2. **Department bonus** — IT 15%, Sales 10%, others 8%; prints bonus and final salary.
3. **Tax calculation** — 10% tax on salaries ≥ ₹50,000, else 5%; shows salary after tax (for salaries above ₹40,000).
4. **Performance bonus** — department-based score (IT 90, Sales 80, others 75) mapped to a 15%/10%/5% bonus.
5. **Summary table** — writes per-employee bonus and final salary into a new `employee_summary` table.
6. **Department totals & averages** — total and average salary for IT, HR, and Sales.
7. **Promotion eligibility** — flags employees earning ≥ ₹50,000 as eligible for promotion.
8. **Salary increment** — calculates incremented salary by department (IT 12%, Sales 10%, others 8%).
9. **Incentive table** — writes slab-based incentives (₹5000 / ₹3000 / ₹2000) into an `employee_incentive` table.
10. **Salary range** — highest salary, lowest salary, and the difference between them.

## Files
- `Solution.py` — the main script with all 10 tasks
- `Supporting_Dataset.sql` — sample dataset to load into MySQL
- `requirements.txt` — Python dependencies

## Run it
1. Load `Supporting_Dataset.sql` into MySQL (it creates the `empolyee` database and `employee_db` table).
2. `pip install -r requirements.txt`
3. `python Solution.py` — you will be asked for your MySQL password; it is never hardcoded in the script.

## Tech
Python · MySQL · SQL · mysql-connector-python
