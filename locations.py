import pandas as pd
import dao

def insertIntoLocations(tableName):

    cnxn = dao.getTargetConnection()
    cursor = cnxn.cursor()

    df = pd.read_csv(f"{tableName}.csv") 
    df.fillna("", inplace=True)

    for index, row in df.iterrows():
        # print(type(row["8"]), row["8"])
        try:
            cursor.execute("""INSERT INTO [dbo].[ST_LOCATIONS]([LOCATION_ID]
                                                    ,[STREET_ADDRESS]
                                                    ,[POSTAL_CODE]
                                                    ,[CITY]
                                                    ,[STATE_PROVINCE]
                                                    ,[COUNTRY_ID]
                                                ) 
                                    values(?,?,?,?,?,?)"""
                                , row["0"], row["1"], row["2"], row["3"], row["4"], row["5"]
                                )
        except Exception as e:
            print(type(str(e)))
            
    cnxn.commit()
    cursor.close()
    cnxn.close()