# ПРОЕКТ
# Парсинг данных по ДТП
## Обработка больших данных в PySpark, кластеризация 
## Сохранение данных в БД

Парсинг данных осуществляется из открытого источника 'https://cms.dtp-stat.ru/media/opendata/'

## СОДЕРЖАНИЕ
[Парсинг данных](#parsing.py)

[Данные в результате парсинга](#папка_data)

[Датасеты](#папка_datasets)

[Обработка данных PySpark Залив в PostgreSQL](#df.ipynb)

## ОПИСАНИЕ ПРОЕКТА

# parsing.py
Универсальный скрипт парсера с сайта 'https://cms.dtp-stat.ru/media/opendata/',
выполняет проверку и закгрузку файлов с геометками и информацией по ДТП по регионам, данные собираются в папку data

# папка_data 
Содержит примеры файлов в формате .geojson  (полный список не возможно выложить в связи с ограничением памяти)

# папка_datasets 
Содержит готовый к работе датафрейм filtered_df.csv (фильтрация по условию ДТП) и датафрейм геоточек центров в результате обработки на PySpark centers.csv

# df.ipynb 
Ноутбук обработки данных из файлов с геоданными, создание отфильтрованного датафрейма, обработка через сервер PySpark, сохранение в СУБД PostgreSQL.

