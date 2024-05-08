CREATE DATABASE IF NOT EXISTS RI;
USE RI;

/* CREATE TABLE IF NOT EXISTS RegistroIndividual (
id_reg int primary key not null auto_increment,
dia_reg varchar(7) not null,
data_reg date not null,
hora_reg time not null,
umidade_solo_reg double not null,
umidade_ambiente_reg double not null,
temperatura_reg double not null,
volume_reg double not null
); */

CREATE TABLE IF NOT EXISTS Usuario(
    id_user int primary key auto_increment not null,
    user_nome varchar(30) not null,
    user_email varchar(30) not null
);