DimLocations	
DimDepartments	
DimEmployees	
DimJobs
DimDate


Create table DimLocations
(
	LocationDimKey		int Identity(1,1)
	,	LocationId		int
	,	StreetAddress	varchar(255)
	,	PostalCode		varchar(255)
	,	City			varchar(50)
	,	State			varchar(50)
	,	CountryName		varchar(50)
    ,	RegionName		varchar(50)
	,	CreatedOn		DateTime2(3) Default getDate()
	,	UpdatedOn		DateTime2(3) Default getDate()
)

Create table DimDepartments
(
	DepartmentsDimKey		int Identity(1,1)
	,	DepartmentId	int
	,	DepartmentName	varchar(50)
	,	CreatedOn		DateTime2(3) Default getDate()
	,	UpdatedOn		DateTime2(3) Default getDate()
)

Create table DimEmployees
(
	EmployeesDimKey		int Identity(1,1)
	,	EmployeeId		int
	,	FirstName		varchar(60)
	,	LastName		varchar(60)
	,	Email			varchar(60)
	,	PhoneNumber		varchar(60)
	,	HireDate		int	
	,	CreatedOn		DateTime2(3) Default getDate()
	,	UpdatedOn		DateTime2(3) Default getDate()
)	

Create table DimManagers
(
	ManagerDimKey		int Identity(1,1)
	,	ManagerId		int
	,	FirstName		varchar(60)
	,	LastName		varchar(60)
	,	Email			varchar(60)
	,	PhoneNumber		varchar(60)
	,	HireDate		int	
	,	CreatedOn		DateTime2(3) Default getDate()
	,	UpdatedOn		DateTime2(3) Default getDate()
)

Create table DimJobs
(
	JobDimKey				int Identity(1,1)
	,	JobId				varchar(60)	
	,	JobTitle			varchar(60)	
	,	MinSalary			int
	,	MaxSalary			int
)


Create Table DimDate
(
	DateDimKey				int
	, calendar_date			varchar(10)
	, month_id				smallint
	, month_desc 			varchar(15)
	, qurater_id			smallint
	, qurater_desc 			varchar(6)
	, year_id 				int
	, day_number_of_week	smallint
	, day_of_week_desc 		varchar(15)
	, day_number_of_month 	smallint
	, day_number_of_year 	smallint
	, week_number_of_year 	smallint
	, year_month 			varchar(7)	
)