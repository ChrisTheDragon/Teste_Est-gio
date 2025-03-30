USE RELATORIO_CADOP;

-- 1. As 10 operadoras com maiores despesas em "EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR" no último trimestre
SELECT 
    o.registro_ans, 
    o.razao_social, 
    SUM(q.vl_saldo_final) AS total_despesas
FROM QUAR_TRI_2024 q
JOIN operadoras_ans o ON q.reg_ans = o.registro_ans
WHERE q.descricao = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR '
GROUP BY o.registro_ans, o.razao_social
ORDER BY total_despesas DESC
LIMIT 10;


-- 2. As 10 operadoras com maiores despesas nessa categoria no último ano (2024)
SELECT 
    o.registro_ans, 
    o.razao_social, 
    SUM(t.vl_saldo_final) AS total_despesas
FROM (
    SELECT reg_ans, vl_saldo_final, descricao FROM PRIM_TRI_2024
    UNION ALL
    SELECT reg_ans, vl_saldo_final, descricao FROM SEC_TRI_2024
    UNION ALL
    SELECT reg_ans, vl_saldo_final, descricao FROM TER_TRI_2024
    UNION ALL
    SELECT reg_ans, vl_saldo_final, descricao FROM QUAR_TRI_2024
) t
JOIN operadoras_ans o ON t.reg_ans = o.registro_ans
WHERE t.descricao = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR '
GROUP BY o.registro_ans, o.razao_social
ORDER BY total_despesas DESC
LIMIT 10;

