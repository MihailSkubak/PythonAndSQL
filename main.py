import pyodbc

connection_to_db = pyodbc.connect(r'Driver={SQL Server};Server=localhost\SQLEXPRESS;Database=KpleadAutomationBase;UID=Kplead;PWD=12345;Trusted_Connection=yes;')
cursor = connection_to_db.cursor()
class BazaDanych:
    def Create(self):
        print('Enter the name of the table for create the table!')
        TableName = input()
        cursor.execute('CREATE TABLE dbo.' + TableName + ' ('
               'id int NOT NULL PRIMARY KEY IDENTITY(1,1),'
               'ID_Number nvarchar(100) UNIQUE, Name nvarchar(50),'
               'AssignedTo nvarchar(50),'
               'Country nvarchar(50),'
               'Status INT '
               ');')
        print('Created')
        connection_to_db.commit()

    def Select(self):
        cursor.execute('SELECT * FROM ACCOUNTS')
        while 1:
            row = cursor.fetchone()
            if not row:
                break
            Name = row.Name
            Login = row.Login
            print(Name)
            print(Login)
    def AlterTable(self):
        print('Enter the name of the table for alter table!')
        TableName = input()
        print('Enter names and data type!')
        Alter = input()
        cursor.execute('ALTER TABLE dbo.' + TableName + ' ADD ' + Alter + ' ;')
        print('Added!')
        connection_to_db.commit()
    def Insert(self):
        print('Enter the name of the table for insert values!')
        TableName = input()
        print('Enter values!')
        Insert = input()
        cursor.execute('INSERT INTO dbo.' + TableName + ' VALUES (' + Insert + ' )')
        print('Added!')
        connection_to_db.commit()

a=BazaDanych()
#a.Select()
#a.Create()
#a.AlterTable()
a.Insert()
connection_to_db.close()
#cursor.execute('SELECT Marka, Model FROM Car')
#while 1:
    #row = cursor.fetchone()
    #if not row:
    #    break
    #print(row.Marka, row.Model)
#connection_to_db.close()
