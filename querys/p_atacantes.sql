SELECT  id,nome  FROM players where clube_id IN (
select casa from partidas, currente_def  where currente_def.clube_id = partidas.visitante order by defesa ASC LIMIT 6) and
posicao_id = 5 and  status = 7 
order by media_num DESC
limit 1 
