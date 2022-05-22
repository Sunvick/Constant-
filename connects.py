import pyodbc

try:
    connect = pyodbc.connect(r'Driver= {Microsoft Access Driver (*.mdb, *.accdb)}; DBQ=C:\Users\raymo\Downloads\Database3.accdb;')
    print("Connected to a Database")

    record = connect.cursor()
    record.execute('select * from tblInventor')
    for row in record.fetchall():
        print(row)

except pyodbc.Error as e:
    print("Error in Connection")