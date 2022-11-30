########################
##    if/else/elif    ##

variavel = "hello world"  # isso é uma variavel, tambem chamada de objeto!
#### daqui pra frente vamos chamar isso de objeto!

if variavel == "hello world":  # trocar depoois o valor pra ver como fica
    print("certinho")
else:
    print("está diferente!")


if True:
    print("sim")

if False:
    print("nunca vai printar isso")

if not False:
    print("isso é a mesma coisa que fazer if True")

#### fazer um input, e checar o tipo do dado
#### usar a lib isinstance  https://www.programiz.com/python-programming/methods/built-in/isinstance

###################
##      for      ##

lista = [1, 2, 3, 4]
lista2 = ["a", "b", "c", "d"]

for item in lista:  # o nome que eu dou ali, item, pode ser qualquer coisa
    print(item)

for qualquer_nome in lista:
    print(qualquer_nome)

print(len(lista))
print(len(lista2))

if len(lista) == len(lista2):
    print("as listas tem o mesmo tamanho!")

for numero in [1, 2, 3, 4]:
    print(numero)


contador = 0
for numero in [1, 2, 3, 4]:
    contador = contador + 1
    print("contador", contador)


for letra in "arthur":
    print("letra", letra)
