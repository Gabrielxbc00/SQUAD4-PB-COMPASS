-- Questão 01
SELECT cod,
       titulo,
       autor,
       editora,
       valor,
       publicacao,
       edicao,
       idioma
FROM livro
WHERE publicacao > '2015-01-01'
ORDER BY cod ASC;


-- Questão 02
SELECT titulo, valor
FROM livro
ORDER BY valor DESC
LIMIT 10;


-- Questão 03
SELECT COUNT(l.cod) as quantidade, e.nome, en.estado, en.cidade
FROM livro l
JOIN editora e ON l.editora = e.codeditora
JOIN endereco en ON e.endereco = en.codendereco
GROUP BY e.nome, en.estado, en.cidade
ORDER BY quantidade DESC
LIMIT 5;


-- Questão 04
SELECT a.codautor, a.nome, a.nascimento, COUNT(l.cod) as quantidade
FROM autor a
LEFT JOIN livro l ON a.codautor = l.autor
GROUP BY a.codautor, a.nome, a.nascimento
ORDER BY a.nome ASC;


-- Questão 05
SELECT DISTINCT A.nome
FROM autor A
JOIN livro L ON A.codautor = L.autor
JOIN editora E ON L.editora = E.codeditora
JOIN endereco EN ON E.endereco = EN.codendereco
WHERE EN.estado NOT IN ('PARANÁ', 'RIO GRANDE DO SUL')
ORDER BY A.nome ASC;


-- Questão 06
SELECT
    a.codautor,
    a.nome,
    COUNT(l.cod) AS quantidade_publicacoes
FROM
    autor a
JOIN
    livro l ON a.codautor = l.autor
GROUP BY
    a.codautor, a.nome
ORDER BY
    quantidade_publicacoes DESC
LIMIT 1;


-- Questão 07
SELECT
    a.nome
FROM
    autor a
LEFT JOIN
    livro l ON a.codautor = l.autor
WHERE
    l.cod IS NULL
ORDER BY
    a.nome ASC;