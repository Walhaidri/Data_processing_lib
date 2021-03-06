# -*- coding: utf-8 -*-
"""
Created on Sat May 28 17:12:36 2022

@author: Walid Al-Haidri

Сегментация сигналов - ипичная задача для обработки и анализа данных 

Например задача: зарегистрированы данные об эпизодах пробуждения пациента 
во время длительного мониторинга сна. Необходимо вырезать сегменты с пробуждения.
Для этого помимио сигнала о процессе сна, прилагает файл-аннотация, где 
0- отмечены эпизоды с нормальным сном
1- эпизоды с нарушением сна
-1 - неопределно
Для понимания смоделированы данные файла-аннотации, а также случайные данные 
о каком-то процессе

"""
import numpy as np
import matplotlib.pyplot as plt

# =============================================================================
# Моделируем слуайные данные мониторинга какого-то процесса, в котором присут
# ствуют несколько состояний
# =============================================================================
n = 1000   # n - количество точек данных
data = np.random.randn(n) # Массив случайных числ

# =============================================================================
# # Моделируем разметку. Для упрощения фрагменты имеют одинаковую длину, но 
# реальные задачи могут иметь разные длинные сегментов разных класслов.
# =============================================================================
annotation = np.zeros(n)

for j in range(100,n,200):
    annotation [j:j+100] = 1

annotation [300:350] = -1

# Визуализируем смоделированные данные + их разметку

plt.plot(data)
plt.plot(annotation ,'-*r')


#%%

# =============================================================================
# Поскольку сегменты могут иметь разную длинную, то  сегменты для каж
#дого типа будем собирать в словарях 
# =============================================================================
z_dic_data = dict()          #  словарь для сбора сегментов класса 0
z_dic_ind = dict()          #  словарь для indexs сегментов класса 0
o_dic_data = dict()          #  словарь для сбора сегментов класса 1
o_dic_ind = dict()          #  словарь для  indexs сегментов класса 1
n_dic_data = dict()          #  словарь для сбора сегментов класса -1
n_dic_ind = dict()          #  словарь для indexs сегментов класса -1


k = 0
while k < len (annotation):
    if annotation[k] == 0:
        zero_ind = [] # список для сбора индексов текущего сегмента класса 0
        zero_val = [] # список для сбора значений элементов текущего сегмента класса 0
        while k < len(annotation) and annotation[k] == 0: # *[1]
            zero_ind.append(k)
            zero_val.append(data[k])
            k += 1
        z_dic_data.setdefault(str(k), zero_val) # После формирования сегмента, добавляем
        # его в словарь
        z_dic_ind.setdefault(str(k), zero_ind) # После формирования сегмента, добавляем
        # его в словарь

    elif annotation[k] == 1:
        one_ind = [] # список для сбора индексов текущего сегмента класса 0
        one_val = [] # список для сбора значений элементов текущего сегмента класса 1
       
        while  k < len(annotation) and annotation[k] == 1:  # *[1]
            one_ind.append(k)
            one_val.append(data[k])
            k += 1     
        o_dic_data.setdefault(str(k), one_val) # После формирования сегмента, добавляем
        # его в словарь
        o_dic_ind.setdefault(str(k), one_ind) # После формирования сегмента, добавляем
        # его в словарь

    else:
       neg_ind = []# список для сбора меток текущего сегмента класса -1(чисто для проверки)
       neg_val = []# список для сбора значений элементов текущего сегмента класса -1
       while  k < len(annotation) and annotation [k] == -1: # *[1]
            neg_ind.append(k)
            neg_val.append(data [k])
            k += 1
       n_dic_data.setdefault( str(k), neg_val) # После формирования сегмента, добавляем
       # его в словарь
       n_dic_ind.setdefault(str(k), neg_ind) # После формирования сегмента, добавляем
       # его в словарь
       
# =============================================================================
# Визуализация с целью проверки работы алгоритма
# =============================================================================
plt.plot(data)  # график сиходных данных
plt.plot(annotation, 'or') # графики разметки
for key in o_dic_data.keys(): #  график фрагментов одного класс
    plt.plot(o_dic_ind[key],o_dic_data[key], 'g' )

# =============================================================================
# *[1] - Дополительно проверяем k < len(annotation) потом что последний 
# локальный к достигает значения len (annotation)
# =============================================================================

