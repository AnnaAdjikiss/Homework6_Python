# Даны два файла в каждом из которых находится запись многочлена. 
# Сформировать файл содержащий сумму многочленов.

import re

def coefs_search(file):
    with open(str(file), 'r') as data:
        pol = data.read()
    print(pol)
    pol = pol.replace('= 0', '')
    pol = re.sub("[*|^| ]", "", pol).split('+')
    pol = [i.split('x') for i in pol]
    for i in pol:
        i[0] = int(i[0]) 
    coefs = [i[0] for i in pol]
    return(coefs)

def res_coefs(coefs1, coefs2):
    sum = []
    for i in range(len(coefs1)):
        sum.append(coefs1[i] + coefs2[i])
    return(sum)

def create_polynom(list, k):
    polynom = [str(list[i]) + '*x^' + str(k-i) for i in range(k-1) if list[i] != 0]
    if list[k-1] != 0:
        polynom.append(str(list[k-1])+'*x')
    if list[k] != 0:
        polynom.append(str(list[k])) 
    return polynom

file1 = 'polynom1.txt' 
file2 = 'polynom2.txt'

sum = res_coefs(coefs_search(file1), coefs_search(file2))
pow = len(sum)-1
result = ' + '.join(create_polynom(sum, pow))  + ' = 0'
print(result)

with open('polynom_res.txt', 'w') as data:
    data.write(result)










