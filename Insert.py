import pyodbc

try:
    connect = pyodbc.connect(
        r'Driver= {Microsoft Access Driver (*.mdb, *.accdb)}; DBQ=C:\Users\raymo\Downloads\Database3.accdb;')
    print("Connected to a Database")

    Inventors = 'ANDRE ISAAC FULGENCIO , CHRISTIAN DALE GUTIERREZ , JAN RUSELL BANTA , JERALPH RED , JOSH GABRIEL SESE , RALPH MICHAEL MOLINA , RAYMOND FRANCIS ARSOLON , SUNVICK GENCIANEO '
    Invention = 'Connecting MS Access Database'
    DateOfInvention = 'May 22, 2022'
    Description = 'We constructed a table of prominent inventors that we could alter using Python and an external connection. We created two "connects" code and "insert" that let us access and input data into the table through Python.'
    user_id = 10

    record = connect.cursor()
    record.execute('UPDATE tblInventor SET Inventors = ? WHERE id=?', (Inventors, user_id))
    record.execute('UPDATE tblInventor SET Invention = ? WHERE id=?', (Invention, user_id))
    record.execute('UPDATE tblInventor SET DateOfInvention = ? WHERE id=?', (DateOfInvention, user_id))
    record.execute('UPDATE tblInventor SET Description = ? WHERE id=?', (Description, user_id))
    record.commit()
    print("Data is updated")

except pyodbc.Error as e:
    print("Error in Connection")