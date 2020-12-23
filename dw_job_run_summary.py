import dao

def insertIntoJobRunSummary(tableName, start_date_Time, end_date_Time, rows_processed, status, error_message, colid, job_run_id):

    cnxn = dao.getTargetConnection()
    cursor = cnxn.cursor()

    try:
        cursor.execute("""INSERT INTO [dbo].[dw_job_run_summary]([tablename]
                                            ,[start_date_Time]
                                            ,[end_date_Time]
                                            ,[rows_processed]
                                            ,[status]
                                            ,[error_message]
                                            ,[colid]
                                            ,[job_run_id]
                                            ) 
                                values(?,?,?,?,?,?,?,?)"""
                            , tableName, start_date_Time, end_date_Time, rows_processed, status, error_message, colid, job_run_id
                            )
    except Exception as e:
        print(type(str(e)))

    cnxn.commit()
    cursor.close()
    cnxn.close()