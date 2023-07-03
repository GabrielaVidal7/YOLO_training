# Transpetro_YOLO
Repositório criado para armazenar os datasets utilizados além dos arquivos necessários para rodar o YOLO.

## Resultados
A partir do dataset presente, utilizou-se YOLOv7. Os resultados obtidos foram:
|                   Name                  |   Train Size  |    Val Size   |   Precision   |    Recall     |      mAP      |
|  -------------------------------------  | ------------- | -------------- | ------------- | ------------- | ------------- |
|           POLI_2023/First_test          |      192      |        53      |     45,1%     |     38,7%     |     35,3%     |
|           POLI_2023/Second_test         |      346      |        86      |     85,0%     |     86,0%     |     90,1%     |
|       Guararema_05_06_23/First_test     |      457      |       130      |     29,5%     |     43,6%     |     32,6%     |
|    Guararema_05_06_23/Second_test/60m   |       45      |        13      |      9,6%     |      4,5%     |      1,4%     |
|    Guararema_05_06_23/Second_test/70m   |      109      |        31      |     91,6%     |     45,5%     |     55,7%     |
|    Guararema_05_06_23/Second_test/80m   |       38      |        11      |      3,5%     |      3,9%     |      3,7%     |
|    Guararema_05_06_23/Second_test/90m   |       34      |         9      |      1,2%     |      2,5%     |      9,7%     |
|   Guararema_05_06_23/Second_test/100m+  |      208      |        59      |     56,4%     |      0,1%     |      2,8%     |
|    Guararema_05_06_23/Third_test/60m    |       85      |        24      |     83,7%     |     37,5%     |     43,3%     |
|    Guararema_05_06_23/Third_test/70m    |      126      |        36      |     ----%     |     ----%     |     ----%     |
|    Guararema_05_06_23/Third_test/80m    |       70      |        20      |      ---%     |      ---%     |      ---%     |
|    Guararema_05_06_23/Third_test/90m    |       73      |        21      |      ---%     |      ---%     |      ---%     |
|   Guararema_05_06_23/Third_test/100m+   |      221      |        63      |     ----%     |      ---%     |      ---%     |

## Folders
A pasta 'POLI_2023/First_test' possui o dataset e resultado do experimento feito com algumas imagens coletadas em 1 dia de vôo pelo campus da USP de São Paulo, na região do Butantã.

A pasta 'POLI_2023/Second_test' possui o dataset e resultado do experimento feito com todas imagens coletadas em 1 dia de vôo pelo campus da USP de São Paulo, na região do Butantã.

A pasta 'Guararema_05_06_23/First_test' possui o dataset e resultado do experimento feito com algumas imagens coletadas em 1 dia de vôo pela região de Guararema, perto da região da empresa em diversas altitudes, de 60m a 120m.

A pasta 'Guararema_05_06_23/Second_test' possui o dataset e resultado dos experimentos feitos com algumas imagens coletadas em 1 dia de vôo pela região de Guararema, perto da região da empresa. Os testes foram divididos de acordo com a altitude de vôo do drone: 60 metros, 70 metros, 80 metros, 90 metros e >=100 metros.

A pasta 'Guararema_05_06_23/Third_test' possui o dataset e resultado dos experimentos feitos com algumas imagens coletadas em 1 dia de vôo pela região de Guararema, perto da região da empresa, e da região do Rio das Ostras (RJ). Os testes foram divididos de acordo com a altitude de vôo do drone: 60 metros, 70 metros, 80 metros, 90 metros e >=100 metros.