import pandas as pd
import dao
import dw_job_run_summary as jobRunSummary
from datetime import datetime

def insertIntoJobHistory(tableName, job_run_id):

    rows_processed = 0
    start_date_Time = datetime.now()
    cnxn = dao.getTargetConnection()
    cursor = cnxn.cursor()
    success  = True

    df = pd.read_csv(f"{tableName}.csv") 
    df.fillna("", inplace=True)

    for index, row in df.iterrows():
        # print(type(row["8"]), row["8"])
        rows_processed += 1
        try:
            cursor.execute("""INSERT INTO [dbo].[ST_JOB_HISTORY]([EMPLOYEE_ID]
                                                ,[START_DATE]
                                                ,[END_DATE]
                                                ,[JOB_ID]
                                                ,[DEPARTMENT_ID]
                                                ) 
                                    values(?,?,?,?,?)"""
                                , row["0"], row["1"], row["2"], row["3"], row["4"]
                                )
        except Exception as e:
            print(type(str(e)))
            success = False
            jobRunSummary.insertIntoJobRunSummary(tableName, start_date_Time, datetime.now(), rows_processed, "Fail", str(e), row["0"], job_run_id)

    if(success):
        jobRunSummary.insertIntoJobRunSummary(tableName, start_date_Time, datetime.now(), rows_processed, "Success", "", "", job_run_id)                                
    cnxn.commit()
    cursor.close()
    cnxn.close()