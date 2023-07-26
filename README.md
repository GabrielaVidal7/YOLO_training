# Transpetro_YOLO
Repositório criado para armazenar os datasets utilizados além dos arquivos necessários para rodar o YOLO.

## Resultados
A partir do dataset presente, utilizou-se YOLOv7. Os resultados obtidos foram:
|                   Name                   |   Train Size  |    Val Size   |   Precision   |    Recall     |      mAP      |
|  --------------------------------------  | ------------- | -------------- | ------------- | ------------- | ------------- |
|            POLI_2023/First_test          |      192      |        53      |     45,1%     |     38,7%     |     35,3%     |
|            POLI_2023/Second_test         |      346      |        86      |     85,0%     |     86,0%     |     **90,1%**     |
|        Guararema_05_06_23/First_test     |      457      |       130      |     29,5%     |     43,6%     |     32,6%     |
|     Guararema_05_06_23/Second_test/60m   |       45      |        13      |      9,6%     |      4,5%     |      1,4%     |
|     Guararema_05_06_23/Second_test/70m   |      109      |        31      |     91,6%     |     45,5%     |     55,7%     |
|     Guararema_05_06_23/Second_test/80m   |       38      |        11      |      3,5%     |      3,9%     |      3,7%     |
|     Guararema_05_06_23/Second_test/90m   |       34      |         9      |      1,2%     |      2,5%     |      9,7%     |
|    Guararema_05_06_23/Second_test/100m+  |      208      |        59      |     56,4%     |      0,1%     |      2,8%     |
|     Guararema_05_06_23/Third_test/60m    |       85      |        24      |     83,7%     |     37,5%     |     43,3%     |
|     Guararema_05_06_23/Third_test/70m    |      126      |        36      |     52,4%     |     38,3%     |     31,5%     |
|     Guararema_05_06_23/Third_test/80m    |       70      |        20      |     90,5%     |     55,6%     |     59,4%     |
|     Guararema_05_06_23/Third_test/90m    |       73      |        21      |     85,7%     |     38,9%     |     47,0%     |
|    Guararema_05_06_23/Third_test/100m+   |      221      |        63      |     38,5%     |      4,4%     |      1,5%     |
|    Guararema_05_06_23/Third_test/Geral   |      662      |       189      |     86,7%     |     80,9%     |     85,6%     |
|     Guararema_e_Arthur/First_test/60m    |     1124      |       321      |     92,5%     |     13,3%     |     15,5%     |
|     Guararema_e_Arthur/First_test/70m    |      915      |       261      |     36,6%     |      8,5%     |      8,2%     |
|     Guararema_e_Arthur/First_test/80m    |       77      |        22      |     %     |     %     |     %     |
|     Guararema_e_Arthur/First_test/90m    |       77      |        22      |     %     |       %     |     %     |
|    Guararema_e_Arthur/First_test/100m+   |      403      |       115      |     %     |      %     |      %     |
|    Guararema_e_Arthur/First_test/Geral   |     2598      |       742      |     %     |       %     |     %     |
|    Guararema_e_Arthur/Second_test/60m    |      396      |       113      |     93,2%     |      37,7%     |    43,1%     |
|    Guararema_e_Arthur/Second_test/70m    |      225      |        64      |     78,2%     |      28,3%     |    23,2%     |
|   Guararema_e_Arthur/Second_test/Geral   |      621      |       177      |      0,9%     |      14,8%     |    19,3%     |

## Folders
A pasta 'POLI_2023/First_test' possui o dataset e resultado do experimento feito com algumas imagens coletadas em 1 dia de vôo pelo campus da USP de São Paulo, na região do Butantã. Somente foi anotado carros.

A pasta 'POLI_2023/Second_test' possui o dataset e resultado do experimento feito com todas imagens coletadas em 1 dia de vôo pelo campus da USP de São Paulo, na região do Butantã. Somente foi anotado os carros das imagens coletadas.

A pasta 'Guararema_05_06_23/First_test' possui o dataset e resultado do experimento feito com algumas imagens coletadas em 1 dia de vôo pela região de Guararema, perto da região da empresa em diversas altitudes, de 60m a 120m. A partir dessa pasta, os dados coletados foram anotados utilizando 4 labels diferentes: pessoas, carros, caminhões e motocicletas.

A pasta 'Guararema_05_06_23/Second_test' possui o dataset e resultado dos experimentos feitos com algumas imagens coletadas em 1 dia de vôo pela região de Guararema, perto da região da empresa. Os testes foram divididos de acordo com a altitude de vôo do drone: 60 metros, 70 metros, 80 metros, 90 metros e >=100 metros.

A pasta 'Guararema_05_06_23/Third_test' possui o dataset e resultado dos experimentos feitos com algumas imagens coletadas em 1 dia de vôo pela região de Guararema, perto da região da empresa, e da região do Rio das Ostras (RJ). Os testes foram divididos de acordo com a altitude de vôo do drone: 60 metros, 70 metros, 80 metros, 90 metros e >=100 metros.

A pasta 'Guararemae_Arthur/First_test' possui o dataset e resultado dos experimentos feitos com algumas imagens coletadas em 1 dia de vôo pela região de Guararema, perto da região da empresa, da região do Rio das Ostras (RJ) e algumas imagens capturadas pelo Arthur da região mais afastada da USP de São Paulo. Os testes foram divididos de acordo com a altitude de vôo do drone: 60 metros, 70 metros, 80 metros, 90 metros e >=100 metros. Com esse último conjunto de dados, a quantidade de imagens de 60m e 70m aumentou mais de 13x. A quantidade de dados gerados a mais para altitudes maiores de 70m não é tão significante. É importante comentar também que, a partir desses dados, existe também a classificação de animais em algumas imagens, totalizando 5 objetos diferentes.

A pasta 'Guararemae_Arthur/Second_test' possui o dataset e resultado dos experimentos feitos com algumas imagens capturadas pelo Arthur da região mais afastada da USP de São Paulo. Os testes foram divididos de acordo com a altitude de vôo do drone: 60 metros e 70 metros. É importante comentar também que, a partir desses dados, existe também a classificação de animais em algumas imagens, totalizando 5 objetos diferentes (pessoas, carros, caminhões, motocicletas e animais).