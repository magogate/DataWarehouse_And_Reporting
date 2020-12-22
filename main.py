import dao
import pandas as pd
import employees as emp
import countries
import departments
import jobHistory
import jobs
import locations
import regions

targetTables = [    
    "REGIONS",
    "COUNTRIES",
    "LOCATIONS",
    "DEPARTMENTS",
    "JOBS",
    "EMPLOYEES",
    "JOB_HISTORY"
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
    if(tableName == "REGIONS"):
        regions.insertIntoRegions(tableName)
    elif(tableName == "COUNTRIES"):
        countries.insertIntoCountries(tableName)
    elif(tableName == "LOCATIONS"):
        locations.insertIntoLocations(tableName)
    elif(tableName == "DEPARTMENTS"):
        departments.insertIntoDepartments(tableName)
    elif(tableName == "JOBS"):
        jobs.insertIntoJobs(tableName)
    elif(tableName == "EMPLOYEES"):
        emp.insertIntoEmployees(tableName)
    elif(tableName == "JOB_HISTORY"):
        jobHistory.insertIntoJobHistory(tableName)
    

for tableName in targetTables:
    fetchRecords(tableName)
    insertRecords(tableName)
    print(tableName)