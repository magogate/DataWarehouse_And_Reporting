# DataWarehouse And Reporting
## Pre-Requisit
1. SQL Server (or any relational database)
2. Python for ETL
3. SSAS / Excel for reporting
4. Sample data of HR schema for this was downloaded from https://github.com/oracle/db-sample-schemas/releases/tag/v12.2.0.1
5. Vishal Studio Code
## Data-Warehouse Flow from Transaction DB till Reporting
Following image depicts data flow of data-warehouse system from Transactional System -> Till Data Warehouse Star Schema and then reporting with different options bassed on DW data.
<img src="DW_Flow_Diagram.jpg" alt="Italian Trulli">
As you can see in diagram 
1. **Transaction DB** -- Data from transaction DB (HR db in this case) we move to staging table first on daily (or weekly / monthly based on need) basis using Full or Incremental Load. In this case we will use Python for ETL, you can use any other tool such as Informatica, SSIS etc. for this.
2. **Staging Table** -- Structure of Staging tables are exactly same as transaction DB, except it has 2 more columns of CreationDate & UpdationDate to document when table was last refreshed. Staging tables are mostly truncate & reload
3. **ODS (Operational Data Source)** -- Data from multiple Staging tables will be combined into single ODS table; also ODS table stores historical data (insert only)
4. **DataWarehouse** -- Data from ODS will be loaded into Dim (Non Measureable Attribute) & Fact (Measurable Attributes) on daily (or weekly / monthly based on need) basis. In this case load from ODS till DW will happen using Stored Proc
5. **Reporting** -- Final reporting will happen using SSAS Cube(Tabular model), Excel Power Pivot, or Power BI. (you can use any tool such as SQL, BO, OBIEE for data analysis)

## Incremental Load
In this case, we are going to use Python for ETL (Extraction Transform Load), and there are 2 ways we are going to see 
1. **Full Load** -- Pulling entire data from source tables to staging tables
2. **Incremental Load** -- Only pulling delta records (updated or newly created records) from source tables to staging tables
We will see difference between these 2 types and when to use each particular type.
Following image ETL using Python which we are going to see in this example
<img src="ETL_UsingPython.jpg" alt="Italian Trulli">

# How to retrieve data from SQL Server using Python
https://stackoverflow.com/questions/51820189/retrieve-data-from-sql-server-database-using-python
```
import pyodbc 
cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                        "Server=mySRVERNAME;"
                        "Database=MYDB;"
                        "uid=sa;pwd=MYPWD;"
                        "Trusted_Connection=yes;")


cursor = cnxn.cursor()
cursor.execute('select DISTINCT firstname,lastname,coalesce(middlename,\' \') as middlename from Person.Person')

for row in cursor:
    print('row = %r' % (row,))
```

# How to read data from Config file using Python
https://stackoverflow.com/questions/19379120/how-to-read-a-config-file-using-python

```
[My Section]
path1 = D:\test1\first
path2 = D:\test2\second
path3 = D:\test2\third
```

```
import ConfigParser

config = ConfigParser.ConfigParser()
config.readfp(open(r'abc.txt'))
path1 = config.get('My Section', 'path1')
path2 = config.get('My Section', 'path2')
path3 = config.get('My Section', 'path3')
```
# ModuleNotFoundError: No module named 'ConfigParser'
https://stackoverflow.com/questions/14087598/python-3-importerror-no-module-named-configparser

# ETL - Load it to Flat File First  
ETL Load from OLTP system to Staging tables can happen by
1. Database to Database -- Both systems - OLTP & Staging - are in different environments, you can directly load data from OLTP to Staging, however, this will keep the connection open to source OLTP till the time load to Staging gets finish. For small datasets, this will work, but if you have millions of records in source, then keeping connection open is not a good idea. 
2. Database to Flag File -- It's always advisable to load data from OLTP to Flat File first and then into Staging. Remember, loading data into (or from) Flat File from OLTP will take considerably less time and this way you don't have to keep your source(or target) connection open for longer period. 

### Creating Multidimentional List
Next task is to get records from database into a list. You can refer code from https://docs.python.org/3.3/tutorial/datastructures.html. 

### Use Pandas Dataframe
Python-Pandas Dataframe is very easy & convenient way to deal with data and for ETL we will use that. You can refer my earlier videos https://youtu.be/ZtXMnCw10Og (2 mins 13 sec) & https://youtu.be/9sjT8EsaoYA (3 mins 58 sec) of using "iloc" of Pandas DataFrame. 

### Use to_csv
Once DataFrame is created, use to_csv methond of python to export data into csv file.
