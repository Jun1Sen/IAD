from klasterizacia import klasterizacia # ����� ������������� ������
from SVM_1 import SVM_1 
from SVM_2 import SVM_2
from regression_analysis import regression_analysis # ������������� ������
from method_loctya import method_loctya  # ����� �����
from random_forest import random_forest # ��������� ���
from testirovanieBD import testirovanieBD # ������������ ��
from IAD import *

# �������� ���� ������� �� ����� �������������� ���������

def main_func():
    # ����� ���� ������������� ������� (��������� � ��� �������, � ������� ���� �� ����� ��������)
    # ���� ���� ����� ������� ����� �� �����������, ������������ ��������� ������� �� ����� ������, ���� ������� � ����, ��� ��������� ������� � ������� ��� ����� 
    klasterizacia()
    SVM_1()
    SVM_2()
    regression_analysis()
    method_loctya()
    random_forest()
    testirovanieBD() # ���� �������