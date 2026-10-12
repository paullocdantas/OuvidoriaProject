
-- BANCO DE DADOS DO SISTEMA DE OUVIDORIA

CREATE DATABASE ouvidoria;

USE ouvidoria;

-- TABELA DE MANIFESTAÇÕES

CREATE TABLE manifestacoes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    protocolo VARCHAR(20),
    nome VARCHAR(100),
    tipo VARCHAR(30),
    descricao TEXT
);
