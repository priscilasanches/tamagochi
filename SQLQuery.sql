CREATE DATABASE Tamagochi
CREATE TABLE TB_MASCOTS
(
NOME VARCHAR (20),
ALTURA TINYINT,
PESO TINYINT,
TIPOS VARCHAR (100),
HABILIDADE VARCHAR (100),
HUMOR TINYINT,
FOME TINYINT,
CANSACO TINYINT,
USUARIO VARCHAR (15)
)

ALTER TABLE TB_MASCOTS ALTER COLUMN NOME VARCHAR(20) NOT NULL

ALTER TABLE TB_MASCOTS ADD CONSTRAINT PK_NOME
PRIMARY KEY CLUSTERED (NOME)

ALTER TABLE TB_MASCOTS ADD DT_ADOCAO DATE
ALTER TABLE TB_MASCOTS ALTER COLUMN DT_ADOCAO DATETIME

SELECT * FROM TB_MASCOTS