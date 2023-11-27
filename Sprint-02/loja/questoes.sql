-- Questão 08
SELECT v.cdvdd, v.nmvdd
FROM tbvendedor v
JOIN tbvendas vd ON v.cdvdd = vd.cdvdd
WHERE vd.status = 'Concluído'
GROUP BY v.cdvdd, v.nmvdd
ORDER BY COUNT(vd.cdven) DESC
LIMIT 1;


-- Questão 09
SELECT v.cdpro, v.nmpro
FROM tbvendas v
WHERE v.dtven BETWEEN '2014-02-03' AND '2018-02-02'
    AND v.status = 'Concluído'
GROUP BY v.cdpro, v.nmpro
ORDER BY SUM(v.qtd) DESC
LIMIT 1;


-- Questão 10
SELECT
    v.nmvdd AS vendedor,
    SUM(vd.vrunt * vd.qtd) AS valor_total_vendas,
    ROUND(SUM(vd.vrunt * vd.qtd) * v.perccomissao / 100, 2) AS comissao
FROM tbvendedor v
LEFT JOIN tbvendas vd ON v.cdvdd = vd.cdvdd AND vd.status = 'Concluído'
GROUP BY v.cdvdd
ORDER BY comissao DESC;


-- Questão 11
SELECT
    vc.cdcli,
    vc.nmcli,
    SUM(vd.qtd * vd.vrunt) AS gasto
FROM
    tbvendas vd
JOIN
    (SELECT cdcli, nmcli FROM tbvendas WHERE status = 'Concluído' GROUP BY cdcli, nmcli) vc
ON
    vd.cdcli = vc.cdcli
GROUP BY
    vc.cdcli, vc.nmcli
ORDER BY
    gasto DESC
LIMIT 1;


-- Questão 12
SELECT
    d.cddep,
    d.nmdep,
    d.dtnasc,
    SUM(v.qtd * v.vrunt) AS valor_total_vendas
FROM
    tbvendedor ve
JOIN
    tbvendas v ON ve.cdvdd = v.cdvdd AND v.status = 'Concluído'
JOIN
    tbdependente d ON ve.cdvdd = d.cdvdd
WHERE
    ve.cdvdd = (
        SELECT
            ve2.cdvdd
        FROM
            tbvendedor ve2
        JOIN
            tbvendas v2 ON ve2.cdvdd = v2.cdvdd AND v2.status = 'Concluído'
        GROUP BY
            ve2.cdvdd
        ORDER BY
            SUM(v2.qtd * v2.vrunt) ASC
        LIMIT 1
    )
GROUP BY
    d.cddep, d.nmdep, d.dtnasc
ORDER BY
    valor_total_vendas;


-- Questão 13
SELECT
    v.cdpro,
    v.nmcanalvendas,
    v.nmpro,
    SUM(v.qtd) AS quantidade_vendas
FROM
    tbvendas v
WHERE
    v.status = 'Concluído'
    AND (v.nmcanalvendas = 'Ecommerce' OR v.nmcanalvendas = 'Matriz')
GROUP BY
    v.cdpro, v.nmcanalvendas, v.nmpro
ORDER BY
    quantidade_vendas
LIMIT 10;


-- Questão 14
SELECT
    estado,
    ROUND(AVG(total_vendas), 2) AS gastomedio
FROM (
    SELECT
        estado,
        cdven,
        SUM(vrunt * qtd) AS total_vendas
    FROM
        tbvendas
    WHERE
        status = 'Concluído'
    GROUP BY
        estado, cdven
) AS subquery
GROUP BY
    estado
ORDER BY
    gastomedio DESC;


-- Questão 15
SELECT cdven
FROM tbvendas
WHERE deletado = '1'
ORDER BY cdven ASC;


-- Questão 16
SELECT
    estado,
    nmpro,
    ROUND(AVG(qtd), 4) AS quantidade_media
FROM tbvendas
WHERE status = 'Concluído'
GROUP BY estado, nmpro
ORDER BY estado, nmpro;

