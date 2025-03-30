CREATE DATABASE IF NOT EXISTS RELATORIO_CADOP;
USE RELATORIO_CADOP;

CREATE TABLE operadoras_ans (
    registro_ans INT PRIMARY KEY,
    cnpj VARCHAR(18) NOT NULL UNIQUE,
    razao_social VARCHAR(150) NOT NULL,
    nome_fantasia VARCHAR(100),
    modalidade VARCHAR(50) NOT NULL,
    logradouro VARCHAR(150) NOT NULL,
    numero VARCHAR(25),
    complemento VARCHAR(50),
    bairro VARCHAR(50) NOT NULL,
    cidade VARCHAR(50) NOT NULL,
    uf CHAR(2) NOT NULL,
    cep VARCHAR(9) NOT NULL,
    ddd VARCHAR(2),
    telefone VARCHAR(20),
    fax VARCHAR(20),
    endereco_eletronico VARCHAR(100),
    representante VARCHAR(100),
    cargo_representante VARCHAR(50),
    regiao_comercializacao VARCHAR(50),
    data_registro_ans DATE NOT NULL
);

LOAD DATA LOCAL INFILE "C:\\Users\\Christian\\Downloads\\Relatorio_CADOP_1.csv"
INTO TABLE operadoras_ans
FIELDS TERMINATED BY ';' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;


CREATE TABLE PRIM_TRI_2023(
    id INT AUTO_INCREMENT PRIMARY KEY,
    data DATE NOT NULL,
    reg_ans INT NOT NULL,
    cd_conta_contabil INT NOT NULL,
    descricao VARCHAR(500) NOT NULL,
    vl_saldo_inicial DECIMAL(20, 2) NOT NULL,
    vl_saldo_final DECIMAL(20, 2) NOT NULL
);

LOAD DATA LOCAL INFILE "C:\\Users\\Christian\\Downloads\\1T2023.csv"
INTO TABLE PRIM_TRI_2023
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ';' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(DATA, REG_ANS, CD_CONTA_CONTABIL, DESCRICAO, @VL_SALDO_INICIAL, @VL_SALDO_FINAL)
SET 
	vl_saldo_inicial = REPLACE(@vl_saldo_inicial, ',', '.'),
    vl_saldo_final = REPLACE(@vl_saldo_final, ',', '.');


CREATE TABLE SEC_TRI_2023(
    id INT AUTO_INCREMENT PRIMARY KEY,
    data DATE NOT NULL,
    reg_ans INT NOT NULL,
    cd_conta_contabil INT NOT NULL,
    descricao VARCHAR(500) NOT NULL,
    vl_saldo_inicial DECIMAL(20, 2) NOT NULL,
    vl_saldo_final DECIMAL(20, 2) NOT NULL
);

LOAD DATA LOCAL INFILE "C:\\Users\\Christian\\Downloads\\2t2023.csv"
INTO TABLE SEC_TRI_2023
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ';' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(DATA, REG_ANS, CD_CONTA_CONTABIL, DESCRICAO, @VL_SALDO_INICIAL, @VL_SALDO_FINAL)
SET 
	vl_saldo_inicial = REPLACE(@vl_saldo_inicial, ',', '.'),
    vl_saldo_final = REPLACE(@vl_saldo_final, ',', '.');


CREATE TABLE TER_TRI_2023(
    id INT AUTO_INCREMENT PRIMARY KEY,
    data DATE NOT NULL,
    reg_ans INT NOT NULL,
    cd_conta_contabil INT NOT NULL,
    descricao VARCHAR(500) NOT NULL,
    vl_saldo_inicial DECIMAL(20, 2) NOT NULL,
    vl_saldo_final DECIMAL(20, 2) NOT NULL
);

LOAD DATA LOCAL INFILE "C:\\Users\\Christian\\Downloads\\3T2023.csv"
INTO TABLE TER_TRI_2023
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ';' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(DATA, REG_ANS, CD_CONTA_CONTABIL, DESCRICAO, @VL_SALDO_INICIAL, @VL_SALDO_FINAL)
SET 
	vl_saldo_inicial = REPLACE(@vl_saldo_inicial, ',', '.'),
    vl_saldo_final = REPLACE(@vl_saldo_final, ',', '.');


CREATE TABLE QUAR_TRI_2023(
    id INT AUTO_INCREMENT PRIMARY KEY,
    data DATE NOT NULL,
    reg_ans INT NOT NULL,
    cd_conta_contabil INT NOT NULL,
    descricao VARCHAR(500) NOT NULL,
    vl_saldo_inicial DECIMAL(20, 2) NOT NULL,
    vl_saldo_final DECIMAL(20, 2)NOT NULL
);

LOAD DATA LOCAL INFILE "C:\\Users\\Christian\\Downloads\\4T2023.csv"
INTO TABLE QUAR_TRI_2023
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ';' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(@DATA, REG_ANS, CD_CONTA_CONTABIL, DESCRICAO, @VL_SALDO_INICIAL, @VL_SALDO_FINAL)
SET 
	vl_saldo_inicial = REPLACE(@vl_saldo_inicial, ',', '.'),
    vl_saldo_final = REPLACE(@vl_saldo_final, ',', '.'),
	data = STR_TO_DATE(@data, '%d/%m/%Y');


CREATE TABLE PRIM_TRI_2024(
    id INT AUTO_INCREMENT PRIMARY KEY,
    data DATE NOT NULL,
    reg_ans INT NOT NULL,
    cd_conta_contabil INT NOT NULL,
    descricao VARCHAR(500) NOT NULL,
    vl_saldo_inicial DECIMAL(20, 2) NOT NULL,
    vl_saldo_final DECIMAL(20, 2)NOT NULL
);

LOAD DATA LOCAL INFILE "C:\\Users\\Christian\\Downloads\\1T2024.csv"
INTO TABLE PRIM_TRI_2024
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ';' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(DATA, REG_ANS, CD_CONTA_CONTABIL, DESCRICAO, @VL_SALDO_INICIAL, @VL_SALDO_FINAL)
SET 
	vl_saldo_inicial = REPLACE(@vl_saldo_inicial, ',', '.'),
    vl_saldo_final = REPLACE(@vl_saldo_final, ',', '.');


CREATE TABLE SEC_TRI_2024(
    id INT AUTO_INCREMENT PRIMARY KEY,
    data DATE NOT NULL,
    reg_ans INT NOT NULL,
    cd_conta_contabil INT NOT NULL,
    descricao VARCHAR(500) NOT NULL,
    vl_saldo_inicial DECIMAL(20, 2) NOT NULL,
    vl_saldo_final DECIMAL(20, 2)NOT NULL
);

LOAD DATA LOCAL INFILE "C:\\Users\\Christian\\Downloads\\2T2024.csv"
INTO TABLE SEC_TRI_2024
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ';' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(DATA, REG_ANS, CD_CONTA_CONTABIL, DESCRICAO, @VL_SALDO_INICIAL, @VL_SALDO_FINAL)
SET 
	vl_saldo_inicial = REPLACE(@vl_saldo_inicial, ',', '.'),
    vl_saldo_final = REPLACE(@vl_saldo_final, ',', '.');


CREATE TABLE TER_TRI_2024(
    id INT AUTO_INCREMENT PRIMARY KEY,
    data DATE NOT NULL,
    reg_ans INT NOT NULL,
    cd_conta_contabil INT NOT NULL,
    descricao VARCHAR(500) NOT NULL,
    vl_saldo_inicial DECIMAL(20, 2) NOT NULL,
    vl_saldo_final DECIMAL(20, 2)NOT NULL
);

LOAD DATA LOCAL INFILE "C:\\Users\\Christian\\Downloads\\3T2024.csv"
INTO TABLE TER_TRI_2024
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ';' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(DATA, REG_ANS, CD_CONTA_CONTABIL, DESCRICAO, @VL_SALDO_INICIAL, @VL_SALDO_FINAL)
SET 
	vl_saldo_inicial = REPLACE(@vl_saldo_inicial, ',', '.'),
    vl_saldo_final = REPLACE(@vl_saldo_final, ',', '.');


CREATE TABLE QUAR_TRI_2024(
    id INT AUTO_INCREMENT PRIMARY KEY,
    data DATE NOT NULL,
    reg_ans INT NOT NULL,
    cd_conta_contabil INT NOT NULL,
    descricao VARCHAR(500) NOT NULL,
    vl_saldo_inicial DECIMAL(20, 2) NOT NULL,
    vl_saldo_final DECIMAL(20, 2)NOT NULL
);

LOAD DATA LOCAL INFILE "C:\\Users\\Christian\\Downloads\\4T2024.csv"
INTO TABLE QUAR_TRI_2024
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ';' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(DATA, REG_ANS, CD_CONTA_CONTABIL, DESCRICAO, @VL_SALDO_INICIAL, @VL_SALDO_FINAL)
SET 
	vl_saldo_inicial = REPLACE(@vl_saldo_inicial, ',', '.'),
    vl_saldo_final = REPLACE(@vl_saldo_final, ',', '.');
    
