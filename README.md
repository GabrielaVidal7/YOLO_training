# Transpetro_YOLO
Repositório criado para armazenar os datasets utilizados além dos arquivos necessários para rodar o YOLO.

## Resultados
A partir do dataset presente, utilizou-se YOLOv7. Os resultados obtidos foram:
|                  Name                 |   Train Size  |    Test Size   |   Precision   |    Recall     |      mAP      |
|  -----------------------------------  | ------------- | -------------- | ------------- | ------------- | ------------- |
|          POLI_2023/First_test         |      192      |        53      |     45,1%     |     38,7%     |     35,3%     |
|          POLI_2023/Second_test        |      346      |        86      |     85,0%     |     86,0%     |     90,1%     |
|      Guararema_05_06_23/First_test    |      457      |       130      |     29,5%     |     43,6%     |     32,6%     |
|   Guararema_05_06_23/Second_test/60m  |       45      |        13      |      9,6%     |      4,5%     |      1,4%     |

## Folders
A pasta 'POLI_2023/First_test' possui o dataset e resultado do experimento feito com algumas imagens coletadas em 1 dia de vôo pelo campus da USP de São Paulo, na região do Butantã.

A pasta 'POLI_2023/Second_test' possui o dataset e resultado do experimento feito com todas imagens coletadas em 1 dia de vôo pelo campus da USP de São Paulo, na região do Butantã.

A pasta 'Guararema_05_06_23/First_test' possui o dataset e resultado do experimento feito com algumas imagens coletadas em 1 dia de vôo pela região de Guararema, perto da região da empresa em diversas altitudes, de 60m a 120m.

A pasta 'Guararema_05_06_23/Second_test' possui o dataset e resultado dos experimentos feitos com algumas imagens coletadas em 1 dia de vôo pela região de Guararema, perto da região da empresa. Os testes foram divididos de acordo com a altitude de vôo do drone: 60 metros, 70 metros, 80 metros, 90 metros e >=100 metros.