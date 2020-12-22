import pandas as pd
import dao

def insertIntoRegions(tableName):

    cnxn = dao.getTargetConnection()
    cursor = cnxn.cursor()

    df = pd.read_csv(f"{tableName}.csv") 
    df.fillna("", inplace=True)

    for index, row in df.iterrows():
        # print(type(row["8"]), row["8"])
        cursor.execute("""INSERT INTO [dbo].[ST_REGIONS]([REGION_ID]
                                             ,[REGION_NAME]
                                            ) 
                                values(?,?)"""
                            , row["0"], row["1"]
                            )
    cnxn.commit()
    cursor.close()
    cnxn.close()