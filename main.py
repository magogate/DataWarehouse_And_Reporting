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

job_run_id = 0

def setJobRunId():
    global job_run_id
    sqlQuery = """select max(job_run_id)
                from [DW].[dbo].[dw_job_run_summary]
                """

    cnxn = dao.getTargetConnection()
    cursor = cnxn.cursor()
    cursor.execute(sqlQuery)

    for row in cursor:        
        print(row) 
        job_run_id = row[0]

    if(job_run_id == None):
        job_run_id = 1
    else:
        job_run_id += 1

    print(f"value of job_run_id is {job_run_id} inside setJobRunId")

    cursor.close()
    cnxn.close()

def truncateTable(tableName):
    sqlQuery = f"truncate table dbo.ST_{tableName}"
    cnxn = dao.getTargetConnection()
    cursor = cnxn.cursor()
    cursor.execute(sqlQuery)
    cnxn.commit()
    cursor.close()
    cnxn.close()

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
        regions.insertIntoRegions(tableName, job_run_id)
    elif(tableName == "COUNTRIES"):
        countries.insertIntoCountries(tableName, job_run_id)
    elif(tableName == "LOCATIONS"):
        locations.insertIntoLocations(tableName, job_run_id)
    elif(tableName == "DEPARTMENTS"):
        departments.insertIntoDepartments(tableName, job_run_id)
    elif(tableName == "JOBS"):
        jobs.insertIntoJobs(tableName, job_run_id)
    elif(tableName == "EMPLOYEES"):
        emp.insertIntoEmployees(tableName, job_run_id)
    elif(tableName == "JOB_HISTORY"):
        jobHistory.insertIntoJobHistory(tableName, job_run_id)
    
setJobRunId()
print(f"value of job_run_id is {job_run_id} after setJobRunId function call")

for tableName in targetTables:
    fetchRecords(tableName)
    truncateTable(tableName)
    insertRecords(tableName)
    print(tableName)