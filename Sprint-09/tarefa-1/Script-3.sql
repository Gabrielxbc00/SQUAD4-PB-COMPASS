-- CRIAÇÃO DA TABELA (Locacao)
CREATE TABLE Locacao (
    idLocacao INT PRIMARY KEY,
    idCliente INT,
    idVendedor INT,
    idCarro INT,
    qtdDiaria INT,
    vlrDiaria DECIMAL(18, 2),
    dataLocacao DATE,
    horaLocacao TIME,
    dataEntrega DATE,
    horaEntrega TIME,
    FOREIGN KEY (idCliente) REFERENCES Cliente(idCliente),
    FOREIGN KEY (idCarro) REFERENCES Carro(idCarro),
    FOREIGN KEY (idVendedor) REFERENCES Vendedor(idVendedor)
);

-- Inserir dados na tabela Locacao
INSERT INTO Locacao (idLocacao, idCliente, idVendedor, idCarro, qtdDiaria, vlrDiaria, dataLocacao, horaLocacao, dataEntrega, horaEntrega)
SELECT idLocacao, idCliente, idVendedor, idCarro, qtdDiaria, vlrDiaria, CAST(dataLocacao AS DATE), CAST(horaLocacao AS TIME), CAST(dataEntrega AS DATE), CAST(horaEntrega AS TIME)
FROM tb_locacao;

-- CRIAÇÃO DA TABELA (CLIENTE)
CREATE TABLE Cliente (
    idCliente INT PRIMARY KEY,
    nomeCliente VARCHAR(100),
    cidadeCliente VARCHAR(40),
    estadoCliente VARCHAR(40),
    paisCliente VARCHAR(40)
);

-- Inserir dados na tabela Cliente
INSERT INTO Cliente (idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente)
SELECT idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente
FROM tb_locacao
GROUP BY idCliente;

-- CRIAÇÃO DA TABELA (CARRO)
CREATE TABLE Carro (
    idCarro INT PRIMARY KEY,
    idCombustivel INT,
    modeloCarro VARCHAR(80),
    marcaCarro VARCHAR(80),
    kmCarro INT,
    anoCarro INT,
    classiCarro VARCHAR(50),
    FOREIGN KEY (idCombustivel) REFERENCES Combustivel(idCombustivel)
);

-- Inserir dados na tabela Carro
INSERT INTO Carro (idCarro, idCombustivel, modeloCarro, marcaCarro, kmCarro, anoCarro, classiCarro)
SELECT idCarro, idcombustivel, modeloCarro, marcaCarro, kmCarro, anoCarro, classiCarro
FROM tb_locacao
GROUP BY idCarro;

-- CRIAÇÃO DA TABELA (COMBUSTIVEL)
CREATE TABLE Combustivel (
    idCombustivel INT PRIMARY KEY,
    tipoCombustivel VARCHAR(20)
);

-- Inserir dados na tabela Combustivel
INSERT INTO Combustivel (idCombustivel, tipoCombustivel)
SELECT idCombustivel, tipoCombustivel
FROM tb_locacao
GROUP BY idCombustivel;

-- CRIAÇÃO DA TABELA (VENDEDOR)
CREATE TABLE Vendedor (
    idVendedor INT PRIMARY KEY,
    nomeVendedor VARCHAR(15),
    sexoVendedor SMALLINT,
    estadoVendedor VARCHAR(40)
);

-- Inserir dados na tabela Vendedor
INSERT INTO Vendedor (idVendedor, nomeVendedor, sexoVendedor, estadoVendedor)
SELECT idVendedor, nomeVendedor, sexoVendedor, estadoVendedor
FROM tb_locacao
GROUP BY idVendedor;