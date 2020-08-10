-- select DEPT_ID_DEP, DEP_NAME from DEPARTMENTS
--     where DEPT_ID_DEP in
--         (select  DEPT_ID_DEP from EMPLOYEES
--             where SALARY > 70000);

-- select * from EMPLOYEES
--     where DEP_ID in
--         (select DEPT_ID_DEP from DEPARTMENTS
--             where DEP_NAME in ('Software Group', 'Design Team'));

select * from EMPLOYEES, DEPARTMENTS
    where DEPT_ID_DEP = DEP_ID;

select min(SALARY) from EMPLOYEES;

select distinct(FIRST_NAME) from INSTRUCTOR;

select F_NAME from EMPLOYEES
    where SALARY =
          (select max(SALARY) from EMPLOYEES);

select * from EMPLOYEES
    where DEP_ID =
          (select max(DEP_ID) from EMPLOYEES);

select F_NAME, DEP_NAME from EMPLOYEES, DEPARTMENTS
    where DEP_ID = DEPT_ID_DEP ;

