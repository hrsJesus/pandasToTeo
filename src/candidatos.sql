SELECT *
FROM tb_candidatura
WHERE
    descricao_situacao_candidatura = '{status_candidatura}'
    AND descricao_cargo NOT LIKE '%{cargo}%'