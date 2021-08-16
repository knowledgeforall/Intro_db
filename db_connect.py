import pyodbc

conn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};"
                      "Server=PAUL-DESKTOP\SQLEXPRESS;"
                      "Database=Are You Not Entertained?;"
                      "Trusted_Connection=yes;")



cursor = conn.cursor()
cursor.execute('SELECT * FROM Video')
for row in cursor:
    print('row = %r' % (row,))


cursor.execute('SELECT * FROM Payment')
for row in cursor:
    print('row = %r' % (row,))

cursor.execute('SELECT * FROM MyVideosList')
for row in cursor:
    print('row = %r' % (row,))

cursor.execute('SELECT * FROM Subscription')
for row in cursor:
    print('row = %r' % (row,))

cursor.execute('SELECT * FROM Search')
for row in cursor:
    print('row = %r' % (row,))

cursor.execute('Insert into AccountsReceivable ([Bank acct #]) values (444444444)')

cursor.execute('SELECT * FROM AccountsReceivable')
for row in cursor:
    print('row = %r' % (row,))

cursor.execute('SELECT * FROM Series')
for row in cursor:
    print('row = %r' % (row,))

cursor.execute('SELECT * FROM Movie')
for row in cursor:
    print('row = %r' % (row,))

cursor.execute('SELECT * FROM Genre')
for row in cursor:
    print('row = %r' % (row,))

cursor.execute('SELECT * FROM UserAcctUserCustomer')
for row in cursor:
    print('row = %r' % (row,))

cursor.execute('SELECT * FROM PaymentInfo')
for row in cursor:
    print('row = %r' % (row,))

cursor.execute('SELECT * FROM Comedy')
for row in cursor:
    print('row = %r' % (row,))

cursor.execute('SELECT * FROM SciFiHorror')
for row in cursor:
    print('row = %r' % (row,))

cursor.execute('SELECT * FROM ActionAdventure')
for row in cursor:
    print('row = %r' % (row,))

cursor.execute('SELECT * FROM Romance')
for row in cursor:
    print('row = %r' % (row,))

cursor.execute('SELECT * FROM Family')
for row in cursor:
    print('row = %r' % (row,))

cursor.execute('SELECT * FROM Drama')
for row in cursor:
    print('row = %r' % (row,))

cursor.execute('SELECT * FROM ForeignFilm')
for row in cursor:
    print('row = %r' % (row,))
    

