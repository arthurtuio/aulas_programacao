import csv

#############################
## criando arquivos vazios ##
with open('arquivo.txtx', 'w') as creating_new_csv_file:
   print("Empty File Created Successfully")


################################################
## dicionario com valores sendo lista pra CSV ##

dicionario = {
    "key1": ['a', 'b', 'c'],
    "key2": ['d', 'e', 'f'],
    "key3": ['g', 'h', 'i']
}
# writing to csv file
with open("test.csv", "w") as outfile:
    # creating a csv writer object
    writerfile = csv.writer(outfile)

    # writing dictionary keys as headings of csv
    writerfile.writerow(dicionario.keys())

    # writing list of dictionary
    writerfile.writerows(zip(*dicionario.values()))


##################################
## lista de dicionarios pra CSV ##

lista_dicionarios = [
    {'name': 'bob', 'age': 25, 'weight': 200},
    {'name': 'jim', 'age': 31, 'weight': 180},
]

keys = lista_dicionarios[0].keys()

with open('test2.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(lista_dicionarios)



##################################
##    lendo csv usando Pandas   ##

import pandas as pd

df = pd.read_csv("/home/arthurantonia/personal_projects/aulas_programacao/modulos/modulo_1-python_basico/aula_3-salvando_dados_como_csv/test2.csv")
print(df)
