-- Create data base Hospital

create database hospital;


create table admin_data(admin_id int primary key auto_increment,
first_name varchar(50),last_name varchar(50),email_id varchar(50) unique ,password_ varchar(50));