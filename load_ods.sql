Create or Alter Procedure load_ods
As
Begin

Declare @ODSRecCount Int;

	select @ODSRecCount = Count(*) from ODS_HR
	if(@ODSRecCount = 0)
	Begin

		insert into ODS_HR( EMPLOYEE_ID 		
						, FIRST_NAME 		
						, LAST_NAME			
						, EMAIL				
						, PHONE_NUMBER		
						, StartDate			
						, EndDate			
						, JOB_ID			
						, MANAGER_ID		
						, DEPARTMENT_ID		
						, DEPARTMENT_NAME	
						, LOCATION_ID		
						, CITY				
						, STATE_PROVINCE	
						, COUNTRY_NAME		
						, REGION_NAME		
					)
			select emp.EMPLOYEE_ID
			, emp.FIRST_NAME
			, emp.LAST_NAME
			, emp.EMAIL
			, emp.PHONE_NUMBER
			, jobhistory.START_DATE 
			, jobhistory.END_DATE 
			, jobhistory.JOB_ID
			, NULL MANAGER_ID
			, jobhistory.DEPARTMENT_ID
			, dep.DEPARTMENT_NAME
			, dep.LOCATION_ID
			, loc.CITY
			, loc.STATE_PROVINCE
			, country.COUNTRY_NAME
			, reg.REGION_NAME
			from ST_JOB_HISTORY jobhistory
			left join ST_EMPLOYEES emp--107
				on jobhistory.EMPLOYEE_ID = emp.EMPLOYEE_ID
			left join ST_DEPARTMENTS dep
				on dep.DEPARTMENT_ID = jobhistory.DEPARTMENT_ID--107
			left join ST_LOCATIONS loc
				on loc.LOCATION_ID = dep.LOCATION_ID
			left join ST_COUNTRIES country
				on country.COUNTRY_ID = loc.COUNTRY_ID
			left join ST_REGIONS reg
				on reg.REGION_ID = country.REGION_ID
			left join ST_JOBS jobs
				on jobs.JOB_ID = emp.JOB_ID

	End;

	begin

		insert into ODS_HR( EMPLOYEE_ID 		
						, FIRST_NAME 		
						, LAST_NAME			
						, EMAIL				
						, PHONE_NUMBER		
						, StartDate			
						, EndDate			
						, JOB_ID			
						, MANAGER_ID		
						, DEPARTMENT_ID		
						, DEPARTMENT_NAME	
						, LOCATION_ID		
						, CITY				
						, STATE_PROVINCE	
						, COUNTRY_NAME		
						, REGION_NAME		
					)
			select emp.EMPLOYEE_ID
			, emp.FIRST_NAME
			, emp.LAST_NAME
			, emp.EMAIL
			, emp.PHONE_NUMBER
			, emp.HIRE_DATE as StartDate
			, NULL as EndDate
			, emp.JOB_ID
			, emp.MANAGER_ID
			, emp.DEPARTMENT_ID
			, dep.DEPARTMENT_NAME
			, dep.LOCATION_ID
			, loc.CITY
			, loc.STATE_PROVINCE
			, country.COUNTRY_NAME
			, reg.REGION_NAME
			from ST_EMPLOYEES emp--107
			left join ST_DEPARTMENTS dep
				on dep.DEPARTMENT_ID = emp.DEPARTMENT_ID--107
			left join ST_LOCATIONS loc
				on loc.LOCATION_ID = dep.LOCATION_ID
			left join ST_COUNTRIES country
				on country.COUNTRY_ID = loc.COUNTRY_ID
			left join ST_REGIONS reg
				on reg.REGION_ID = country.REGION_ID
			left join ST_JOBS jobs
				on jobs.JOB_ID = emp.JOB_ID
			where 1=1
			and not exists(
				select 1
				from ODS_HR ods
				where 1=1
				and ods.EMPLOYEE_ID = emp.EMPLOYEE_ID
				and ods.StartDate = emp.HIRE_DATE
				and ods.JOB_ID = emp.JOB_ID
				and ods.DEPARTMENT_ID = emp.DEPARTMENT_ID
			)



			Update ods
			set ods.FIRST_NAME = Emp.FIRST_NAME
			, ods.LAST_NAME = Emp.LAST_NAME
			, ods.EMAIL = Emp.EMAIL
			, ods.PHONE_NUMBER = Emp.PHONE_NUMBER		
			, ods.UpdatedOn = GETDATE()
			from ODS_HR ods
			join (
				select emp.EMPLOYEE_ID
				, emp.FIRST_NAME
				, emp.LAST_NAME
				, emp.EMAIL
				, emp.PHONE_NUMBER
				, emp.HIRE_DATE as StartDate
				, NULL as EndDate
				, emp.JOB_ID
				, emp.MANAGER_ID
				, emp.DEPARTMENT_ID
				, dep.DEPARTMENT_NAME
				, dep.LOCATION_ID
				, loc.CITY
				, loc.STATE_PROVINCE
				, country.COUNTRY_NAME
				, reg.REGION_NAME
				from ST_EMPLOYEES emp--107
				left join ST_DEPARTMENTS dep
					on dep.DEPARTMENT_ID = emp.DEPARTMENT_ID--107
				left join ST_LOCATIONS loc
					on loc.LOCATION_ID = dep.LOCATION_ID
				left join ST_COUNTRIES country
					on country.COUNTRY_ID = loc.COUNTRY_ID
				left join ST_REGIONS reg
					on reg.REGION_ID = country.REGION_ID
				left join ST_JOBS jobs
					on jobs.JOB_ID = emp.JOB_ID
			)Emp			
				on ods.EMPLOYEE_ID = Emp.EMPLOYEE_ID
				and ods.StartDate = Emp.StartDate
				and ods.JOB_ID = Emp.JOB_ID
				and ods.DEPARTMENT_ID = Emp.DEPARTMENT_ID
	End;


End;


