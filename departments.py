import pandas as pd
import dao

def insertIntoDepartments(tableName):

    cnxn = dao.getTargetConnection()
    cursor = cnxn.cursor()

    df = pd.read_csv(f"{tableName}.csv") 
    df.fillna("", inplace=True)

    for index, row in df.iterrows():
        # print(type(row["8"]), row["8"])
        cursor.execute("""INSERT INTO [dbo].[ST_DEPARTMENTS]([DEPARTMENT_ID]
                                            ,[DEPARTMENT_NAME]
                                            ,[MANAGER_ID]
                                            ,[LOCATION_ID]
                                            ) 
                                values(?,?,?,?)"""
                            , row["0"], row["1"], row["2"], row["3"]
                            )
    cnxn.commit()
    cursor.close()
    cnxn.close()