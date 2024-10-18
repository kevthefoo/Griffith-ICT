/* The COMPANY database schema (based on the textbook) */

USE company;

/* Fill in data */

/* must use a trick to get around fks cross-referencing employee and department */
/* put in NULL values at first for dept manager ssn */

insert into department values ('Research', 5, NULL , '1978-05-22');

insert into department values ('Administration', 4, NULL , '1985-01-01');

insert into department values ('Headquarters', 1, NULL , '1971-06-19');


insert into employee values
    ('James Borg', '888665555', '1927-11-10', '450 Stone, Houston, TX',
     'M', 55000, null, 1);

insert into employee values
    ('Franklin Wong', '333445555', '1945-12-08', '638 Voss, Houston, TX',
     'M', 40000, '888665555', 5);

insert into employee values
    ('Jennifer Wallace', '987654321', '1931-06-20', '291 Berry, Bellaire, TX',
     'F', 43000, '888665555', 4);

insert into employee values
    ('Ahmad Jabbar', '987987987', '1959-03-29', '980 Dallas, Houston, TX',
     'M', 25000, '987654321', 4);

insert into employee values
    ('John Smith', '123456789', '1955-01-09', '731 Fondren, Houston, TX', 
     'M', 30000, '333445555', 5);

insert into employee values
    ('Alicia Zelaya', '999887777', '1958-07-19', '3321 Castle, Spring, TX',
     'F', 25000, '987654321', 4);

insert into employee values
    ('Ramesh Narayan', '666884444', '1952-09-15', '975 Fire Oak, Humble, TX',
     'M', 38000, '333445555', 5);

insert into employee values
    ('Joyce English', '453453453', '1962-07-31', '5631 Rice, Houston, TX',
     'F', 25000, '333445555', 5);

/* now add the dept manager ssns */

update department
   set mgrssn = '333445555' where dnumber=5;

update department
   set mgrssn = '987654321' where dnumber=4;

update department
   set mgrssn = '888665555' where dnumber=1;


insert into dept_locations values (1, 'Houston');
insert into dept_locations values (4, 'Stafford');
insert into dept_locations values (5, 'Bellaire');
insert into dept_locations values (5, 'Sugarland');
insert into dept_locations values (5, 'Houston');

insert into project values ('ProductX', 1, 'Bellaire', 5);
insert into project values ('ProductY', 2, 'Sugarland', 5);
insert into project values ('ProductZ', 3, 'Houston', 5);
insert into project values ('Computerization', 10, 'Stafford', 4);
insert into project values ('Reorganization', 20, 'Houston', 1);
insert into project values ('Newbenefits', 30, 'Stafford', 4);


insert into works_on values ('123456789', 1, 32.5);
insert into works_on values ('123456789', 2, 7.5);
insert into works_on values ('666884444', 3, 40.0);
insert into works_on values ('453453453', 1, 20.0);
insert into works_on values ('453453453', 2, 20.0);
insert into works_on values ('333445555', 2, 10.0);
insert into works_on values ('333445555', 3, 10.0);
insert into works_on values ('333445555', 10, 10.0);
insert into works_on values ('333445555', 20, 10.0);
insert into works_on values ('999887777', 30, 30.0);
insert into works_on values ('999887777', 10, 10.0);
insert into works_on values ('987987987', 10, 35.0);
insert into works_on values ('987987987', 30, 5.0);
insert into works_on values ('987654321', 30, 20.0);
insert into works_on values ('987654321', 20, 15.0);
insert into works_on values ('888665555', 20, NULL);


insert into dependent values
    ('333445555', 'Alice', 'F', '1976-04-05','Daughter');
insert into dependent values
    ('333445555', 'Theodore', 'M', '1973-10-25', 'Son');
insert into dependent values
    ('333445555', 'Joy', 'F', '1948-05-03', 'Spouse');
insert into dependent values
    ('987654321', 'Abner', 'M', '1932-02-29', 'Spouse');
insert into dependent values 
    ('123456789', 'Michael', 'M', '1978-01-01', 'Son');
insert into dependent values
    ('123456789', 'Alice', 'F', '1972-12-31', 'Daughter');
insert into dependent values
    ('123456789', 'Elizabeth', 'F', '1957-05-05', 'Spouse');

