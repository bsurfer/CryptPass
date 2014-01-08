
--DROP TABLE IF EXISTS information 

create table if not exists information (
id integer primary key, 
name varchar(50), 
user varchar(50), 
password varchar(50)
);
