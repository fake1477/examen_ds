drop database Universidad;

create database Universidad;

use Universidad;

create table profesores (
  id int(5) NOT NULL primary key auto_increment,
  nombre varchar(50) NOT NULL,
  codigo int(50) NOT NULL,
  username varchar(50) NOT NULL,
  password varchar(50) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=100 DEFAULT CHARSET=latin1;

create table alumnos (
  id int(5) NOT NULL primary key auto_increment,
  nombre varchar(50) NOT NULL,
  codigo int(50) NOT NULL,
  username varchar(50) NOT NULL,
  password varchar(50) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=100 DEFAULT CHARSET=latin1;