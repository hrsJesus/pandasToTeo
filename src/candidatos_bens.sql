SELECT
    t1.*,
    COALESCE(t2.total_declarado, 0) AS total_declarado,
    COALESCE(t2.qtde_itens_declarados, 0) AS qtde_itens_declarados
FROM tb_candidatura t1
LEFT JOIN (
    select
        numero_sequencial,
        sum( valor ) total_declarado,
        count( 1 ) qtde_itens_declarados
    from tb_declaracao_2018
    group by numero_sequencial
) t2
on t1.numero_sequencial = t2.numero_sequencial
WHERE
    numero_turno = 1
    AND descricao_situacao_candidatura = 'APTO'
    AND descricao_cargo LIKE '%{cargo}%'