ALTER TABLE dbo.Countries
alter column COUNTRY_ID nvarchar(255) NOT NULL

ALTER TABLE dbo.Countries
ADD CONSTRAINT PK_Countries PRIMARY KEY (Country_ID);

ALTER TABLE dbo.Countries
ADD CONSTRAINT FK_RegionId
FOREIGN KEY (Region_Id) REFERENCES REGIONS(Region_Id);

ALTER TABLE Dbo.DEPARTMENTS
alter column department_id float NOT NULL

ALTER TABLE Dbo.DEPARTMENTS
ADD CONSTRAINT PK_Departments PRIMARY KEY (department_id);

ALTER TABLE dbo.Departments
ADD CONSTRAINT FK_LocationId
FOREIGN KEY (Location_Id) REFERENCES LOCATIONS(Location_Id);

ALTER TABLE dbo.EMPLOYEES 
alter column employee_id float NOT NULL

ALTER TABLE dbo.EMPLOYEES 
ADD CONSTRAINT PK_Employees PRIMARY KEY (employee_id);

ALTER TABLE dbo.Employees
ADD CONSTRAINT FK_DepartmentId
FOREIGN KEY (Department_Id) REFERENCES Departments(Department_Id);

ALTER TABLE dbo.Employees
ADD CONSTRAINT FK_JOBid
FOREIGN KEY (Job_Id) REFERENCES Jobs(Job_Id);


ALTER TABLE JOBS
alter column JOB_ID nvarchar(255) NOT NULL

ALTER TABLE JOBS
ADD CONSTRAINT PK_JObs PRIMARY KEY (job_id);


alter table dbo.locations
alter column location_id float NOT NULL

alter table dbo.locations
ADD CONSTRAINT PK_Locations PRIMARY KEY (location_id);

ALTER TABLE dbo.Locations
ADD CONSTRAINT FK_CountryId
FOREIGN KEY (Country_Id) REFERENCES Countries(Country_Id);


alter table dbo.REGIONS
alter column REGION_ID float NOT NULL

alter table dbo.REGIONS
ADD CONSTRAINT PK_Regions PRIMARY KEY (Region_id);



ALTER TABLE dbo.JOB_HISTORY
ADD CONSTRAINT FK_Emp
FOREIGN KEY (Employee_Id) REFERENCES Employees(Employee_Id);


ALTER TABLE dbo.JOB_HISTORY
ADD CONSTRAINT FK_Dep
FOREIGN KEY (Department_Id) REFERENCES Departments(Department_Id);


ALTER TABLE dbo.JOB_HISTORY
ADD CONSTRAINT FK_JOB
FOREIGN KEY (JOB_Id) REFERENCES Jobs(JOB_Id);