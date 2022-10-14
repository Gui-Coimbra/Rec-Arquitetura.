CREATE USER 'crawler'@'localhost' IDENTIFIED BY 'sptech';
GRANT SELECT, UPDATE, INSERT, DELETE, EXECUTE, SHOW VIEW ON webcrawler.* TO 'crawler'@'localhost';

CREATE DATABASE webcrawler;
USE webcrawler;

drop table clima;
CREATE TABLE clima(
id int primary key auto_increment,
id_municipio int,
id_estacao varchar(10),
estacao varchar(45),
data_fundacao date,
latitude varchar(30),
longitude varchar(30),
altitude varchar(30)
);

explain select * from clima;