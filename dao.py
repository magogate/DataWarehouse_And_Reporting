import pyodbc 
import configparser

def getSourceConnection():
    config = configparser.ConfigParser()
    config.readfp(open(r'config.ini'))

    DSN = config.get('DB_Source', 'DSN')
    DB = config.get('DB_Source', 'DB')
    UID = config.get('DB_Source', 'UID')
    PWD = config.get('DB_Source', 'PWD')

    cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                            f"Server={DSN};"
                            f"Database={DB};"
                            f"uid={UID};pwd={PWD};"
                            "Trusted_Connection=yes;")

    return cnxn

def getTargetConnection():
    config = configparser.ConfigParser()
    config.readfp(open(r'config.ini'))

    DSN = config.get('DB_Target', 'DSN')
    DB = config.get('DB_Target', 'DB')
    UID = config.get('DB_Target', 'UID')
    PWD = config.get('DB_Target', 'PWD')

    cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                            f"Server={DSN};"
                            f"Database={DB};"
                            f"uid={UID};pwd={PWD};"
                            "Trusted_Connection=yes;")

    return cnxn    