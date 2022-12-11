CREATE DATABASE notapp;

USE notapp;

CREATE TABLE USUARIOS (
    id_usuario int(8),
    usuario varchar(50),
    pass varchar(128),
    email varchar(254));
    
CREATE TABLE NOTAS (
    id_nota int(8),
    id_usuario int(8),
    titulo varchar(100),
    contenido varchar(500),
    cumplido int(1));

ALTER TABLE USUARIOS
    CHANGE `id_usuario` `id_usuario` INT(8) NOT NULL AUTO_INCREMENT, 
    ADD PRIMARY KEY(id_usuario);
ALTER TABLE NOTAS
    CHANGE `id_nota` `id_nota` INT(8) NOT NULL AUTO_INCREMENT, 
    ADD PRIMARY KEY(id_nota);

ALTER TABLE NOTAS
    ADD FOREIGN KEY (id_usuario) REFERENCES USUARIOS(id_usuario);