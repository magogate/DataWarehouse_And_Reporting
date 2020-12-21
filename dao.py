import pyodbc 
import configparser

def getSourceConnection():
    config = configparser.ConfigParser()
    config.readfp(open(r'config.ini'))

    DSN = config.get('DB', 'DSN')
    DB = config.get('DB', 'DB')
    UID = config.get('DB', 'UID')
    PWD = config.get('DB', 'PWD')

    cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                            f"Server={DSN};"
                            f"Database={DB};"
                            f"uid={UID};pwd={PWD};"
                            "Trusted_Connection=yes;")

    cursor = cnxn.cursor()

    return cursor