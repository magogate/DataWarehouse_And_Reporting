import dao
import pandas as pd
import employees as emp

targetTables = [    
    # "REGIONS",
    # "COUNTRIES",
    # "LOCATIONS",
    # "DEPARTMENTS",
    # "JOBS",
    "EMPLOYEES"
    # "JOB_HISTORY"
]

def fetchRecords(tableName):

    sqlQuery = f"""
                    select *
                    from {tableName}
                    where 1=1
                """    

    cnxn = dao.getSourceConnection()
    cursor = cnxn.cursor()
    cursor.execute(sqlQuery)

    hrList = []
    for row in cursor:        
        hrList.append([elem for elem in row])        

    pd.DataFrame(hrList).iloc[:,:].to_csv(f"{tableName}.csv", index=False)

    cursor.close()
    cnxn.close()

def insertRecords(tableName):
    emp.insertIntoEmployees(tableName)
    

for tableName in targetTables:
    fetchRecords(tableName)
    insertRecords(tableName)
    print(tableName)