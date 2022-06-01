CREATE DATABASE IF NOT EXISTS bd_agendamento;


use bd_agendamento;


create TABLE clientes(id_cliente integer PRIMARY KEY AUTO_INCREMENT NOT NULL, 
                        nome_cliente varchar(60), 
                        cpf varchar(11), 
                        email_cliente varchar(50), 
                        telefone varchar(20), 
                         senha varchar(30))

