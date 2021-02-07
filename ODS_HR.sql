Create table ODS_HR
(
	id 					int IDENTITY(1,1) PRIMARY KEY
	, EMPLOYEE_ID 		int 
	, FIRST_NAME 		varchar(50)
    , LAST_NAME			varchar(50)
    , EMAIL				varchar(60)
    , PHONE_NUMBER		varchar(30)
    , StartDate			DateTime2(3)
	, EndDate			DateTime2(3)
    , JOB_ID			varchar(30)
    , MANAGER_ID		int 
    , DEPARTMENT_ID		int	
    , DEPARTMENT_NAME	varchar(50)
    , LOCATION_ID		int
    , CITY				varchar(50)
    , STATE_PROVINCE	varchar(50)	
	, COUNTRY_NAME		varchar(50)	
	, REGION_NAME		varchar(50)	
	, CreatedOn			DateTime2(3) DEFAULT getDate()
	, UpdatedOn			DateTime2(3) DEFAULT getDate()
)