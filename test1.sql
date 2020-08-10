-- select DEPT_ID_DEP, DEP_NAME from DEPARTMENTS
--     where DEPT_ID_DEP in
--         (select  DEPT_ID_DEP from EMPLOYEES
--             where SALARY > 70000);

-- select * from EMPLOYEES
--     where DEP_ID in
--         (select DEPT_ID_DEP from DEPARTMENTS
--             where DEP_NAME in ('Software Group', 'Design Team'));

select * from DEPARTMENTS, EMPLOYEES;