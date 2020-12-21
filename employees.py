import pandas as pd
import dao

def insertIntoEmployees(tableName):

    cnxn = dao.getTargetConnection()
    cursor = cnxn.cursor()

    df = pd.read_csv(f"{tableName}.csv") 
    df.fillna("", inplace=True)

    for index, row in df.iterrows():
        # print(type(row["8"]), row["8"])
        cursor.execute("""INSERT INTO [dbo].[ST_EMPLOYEES]([EMPLOYEE_ID]
                                            ,[FIRST_NAME]
                                            ,[LAST_NAME]
                                            ,[EMAIL]
                                            ,[PHONE_NUMBER]
                                            ,[HIRE_DATE]
                                            ,[JOB_ID]
                                            ,[SALARY]
                                            ,[COMMISSION_PCT]
                                            ,[MANAGER_ID]
                                            ,[DEPARTMENT_ID]
                                            ) 
                                values(?,?,?,?,?,?,?,?,?,?,?)"""
                            , row["0"], row["1"], row["2"]
                            , row["3"], row["4"], row["5"]
                            , row["6"], row["7"], row["8"]
                            , row["9"], row["10"]
                            )
    cnxn.commit()
    cursor.close()
    cnxn.close()