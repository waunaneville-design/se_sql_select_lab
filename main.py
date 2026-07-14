import sqlite3
import pandas as pd

# STEP 1A
# Import SQL Library and Pandas

# STEP 1B
# Connect to the database
conn = sqlite3.connect('data.sqlite')

# STEP 2
# Replace None with your code
df_first_five = pd.read_sql("""
SELECT employeeNumber, lastName
FROM employees
""", conn)

# STEP 3
# Replace None with your code
df_five_reverse = pd.read_sql("""
SELECT lastName, employeeNumber
FROM employees
""", conn)

# STEP 4
# Replace None with your code
df_alias = pd.read_sql("""
SELECT employeeNumber AS ID, lastName
FROM employees
""", conn)

