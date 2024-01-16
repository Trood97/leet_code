

import sqlite3

# Connect to the SQLite database (or create a new one if it doesn't exist)
conn = sqlite3.connect('mydatabase1.db')
cursor = conn.cursor()

# # Read data from the table
# cursor.execute("SELECT * FROM employees")
# rows = cursor.fetchall()
# print("Employees:")
# for row in rows:
#     print(row)
#
# # Update data in the table
# cursor.execute("UPDATE employees SET salary = ? WHERE name = ?", (85000.00, 'John Doe'))
# conn.commit()

# # Read the updated data
# cursor.execute("SELECT * FROM employees")
# rows = cursor.fetchall()
# print("\nUpdated Employees:")
# for row in rows:
#     print(row)
#
# # Delete data from the table
# cursor.execute("DELETE FROM employees WHERE name = ?", ('Jane Doe',))
# conn.commit()
#
# # Read the remaining data
# cursor.execute("SELECT * FROM employees")
# rows = cursor.fetchall()
# print("\nRemaining Employees:")
# for row in rows:
#     print(row)
#
# # Close the connection
# conn.close()
