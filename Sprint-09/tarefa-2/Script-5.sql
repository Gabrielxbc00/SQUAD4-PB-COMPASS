-- Quantos carros cada vendedor alugou

-- View para a Dimensão Vendedor
CREATE VIEW Dimensao_vendedor AS
SELECT idVendedor, nomeVendedor, estadoVendedor
FROM Vendedor;

-- View para a Dimensão Data
CREATE VIEW Dimensao_data AS
SELECT DISTINCT dataLocacao AS Data
FROM Locacao;

-- View para a Tabela Locacao
CREATE VIEW aluguel_vendedor AS
SELECT
    L.idVendedor,
    V.nomeVendedor,
    D.Data,
    COUNT(L.idCarro) AS QtdCarrosAlugados
FROM Locacao L
JOIN Dimensao_vendedor V ON L.idVendedor = V.idVendedor
JOIN Dimensao_data D ON L.dataLocacao = D.Data
GROUP BY L.idVendedor, V.nomeVendedor, D.Data;

-- Verificando a resposta à pergunta
SELECT * FROM aluguel_vendedor;
