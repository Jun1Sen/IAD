from klasterizacia import klasterizacia # метод кластеризации данных
from SVM_1 import SVM_1 
from SVM_2 import SVM_2
from regression_analysis import regression_analysis # регрессионный анализ
from method_loctya import method_loctya  # метод локтя
from random_forest import random_forest # случайный лес
from testirovanieBD import testirovanieBD # тестирование БД
from IAD import *

# основной файл запуска со всеми реализованными функциями

def main_func():
    # Вызов всех реализованных функций (Расположи в том порядке, в котором тебе их нужно вызывать)
    # Если тебе нужно вызвать метод по отдельности, закомментруй остальные функции на время вызова, либо перейди в файл, где находится функция и пропиши там вызов 
    klasterizacia()
    SVM_1()
    SVM_2()
    regression_analysis()
    method_loctya()
    random_forest()
    testirovanieBD() # тест коммент