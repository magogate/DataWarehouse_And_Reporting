import dao
import pandas as pd
import employees as emp
import countries
import departments
import jobHistory
import jobs
import locations
import regions
import dw_job_run_summary as jobRunSummary
from datetime import datetime


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
lastJobRunDate = '2021-02-20'
rows_processed = 0
start_date_Time = datetime.now()

def getLastJobRunDate(tableName):    
    global lastJobRunDate
    sqlQuery = f"""select cast(max(start_date_Time) as date) as lastJobRunDate
                    from [DW].[dbo].[dw_job_run_summary]
                    where 1=1
                    and job_run_id in(
                        select max(job_run_id)
                        from [DW].[dbo].[dw_job_run_summary]
                        where 1=1                
                        and tablename = '{tableName}'
                        )
                    and tablename = '{tableName}'
                """

    print(lastJobRunDate)

    cnxn = dao.getTargetConnection()
    cursor = cnxn.cursor()
    cursor.execute(sqlQuery)

    for row in cursor:        
        # print(row) 
        lastJobRunDate = row[0]

    if(job_run_id == None):
        lastJobRunDate = '1900-01-01'    

    # print(f"value of job_run_id is {job_run_id} inside setJobRunId")

    cursor.close()
    cnxn.close()

def setJobRunId():
    global job_run_id
    sqlQuery = """select max(job_run_id)
                from [DW].[dbo].[dw_job_run_summary]
                """

    cnxn = dao.getTargetConnection()
    cursor = cnxn.cursor()
    cursor.execute(sqlQuery)

    for row in cursor:        
        # print(row) 
        job_run_id = row[0]

    if(job_run_id == None):
        job_run_id = 1
    else:
        job_run_id += 1

    # print(f"value of job_run_id is {job_run_id} inside setJobRunId")

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

    if(tableName == "EMPLOYEES"):
        sqlQuery = f"""
                        select *
                        from {tableName}
                        where 1=1
                        and (CreatedOn >= DateAdd(dd, -3, '{lastJobRunDate}')
                            or UpdatedOn >= DateAdd(dd, -3, '{lastJobRunDate}')
                        )
                    """    
    elif(tableName == "DEPARTMENTS"):
        sqlQuery = f"""
                    select *
                    from DEPARTMENTS
					where DEPARTMENT_ID in(
                        select DEPARTMENT_ID
                        from EMPLOYEES
                        where 1=1
                        and (CreatedOn >= DateAdd(dd, -3, '{lastJobRunDate}')
                            or UpdatedOn >= DateAdd(dd, -3, '{lastJobRunDate}')
                        )
                    )
                """    
    else:
        sqlQuery = f"""
                        select *
                        from {tableName}
                        where 1=1                        
                    """            
        

    print(sqlQuery)

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
    try:
        df = pd.read_csv(f"{tableName}.csv") 

        if(tableName == "REGIONS"):
            regions.insertIntoRegions(df, tableName, job_run_id)
        elif(tableName == "COUNTRIES"):
            countries.insertIntoCountries(df, tableName, job_run_id)
        elif(tableName == "LOCATIONS"):
            locations.insertIntoLocations(df, tableName, job_run_id)
        elif(tableName == "DEPARTMENTS"):
            departments.insertIntoDepartments(df, tableName, job_run_id)
        elif(tableName == "JOBS"):
            jobs.insertIntoJobs(df, tableName, job_run_id)
        elif(tableName == "EMPLOYEES"):
            emp.insertIntoEmployees(df, tableName, job_run_id)
        elif(tableName == "JOB_HISTORY"):
            jobHistory.insertIntoJobHistory(df, tableName, job_run_id)

    except Exception as e:                        
            jobRunSummary.insertIntoJobRunSummary(tableName, start_date_Time, datetime.now(), rows_processed, "Fail", str(e), 0, job_run_id)
    
setJobRunId()
# print(f"value of job_run_id is {job_run_id} after setJobRunId function call")

for tableName in targetTables:
    getLastJobRunDate(tableName)
    fetchRecords(tableName)
    truncateTable(tableName)
    insertRecords(tableName)
    print(tableName)