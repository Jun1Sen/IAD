import requests
import os
import pandas as pd
from sqlalchemy import create_engine

# Функция для загрузки данных о ДТП с сайта ГИБДД
def download_accident_data(save_path):
    url = 'http://stat.gibdd.ru/'
    response = requests.get(url)
    with open(save_path, 'wb') as f:
        f.write(response.content)


# Получение названия файла от пользователя
file_name = input("Введите название файла для сохранения данных (без расширения): ")
save_path = file_name + '.xlsx'

# Вызов функции для загрузки данных о ДТП
download_accident_data(save_path)
