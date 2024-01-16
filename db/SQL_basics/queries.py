# conn=
# cursor =


#creating a table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS EmployeeInfo  (
        EmpID INTEGER PRIMARY KEY,
        EmpFname TEXT NOT NULL,
        EmpLname TEXT NOT NULL,
        Department TEXT NOT NULL,
        Project TEXT NOT NULL,
        Address TEXT NOT NULL,
        DOB VARCHAR(10),
        Gender VARCHAR(1)
    )

#insertion
conn.execute('''INSERT INTO EmployeeInfo (EmpId, EmpFname, EmpLname, Department, Project, Address, DOB, Gender)
VALUES
    (1, 'Anand', 'Ballidaw', 'Tech', 'ds', 'k.nagar', '2011-11-11', 'M'),
    (2, 'Spider', '.', 'Tech', 'sde', 'v.nagar', '2010-11-01', 'M'),
    (3, 'Rix', '-', 'Management', 'pm', 't.nagar', '2000-11-02', 'F');'''
)