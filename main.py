import dao

cursor = dao.getSourceConnection()

cursor.execute('SELECT [JOB_TITLE] ,[MIN_SALARY] ,[MAX_SALARY]  FROM [HR].[dbo].[JOBS]')

for row in cursor:
    print('row = %r' % (row,))