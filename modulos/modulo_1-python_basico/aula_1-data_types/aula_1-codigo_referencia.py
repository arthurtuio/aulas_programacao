# isso é um comentário

###################
##    strings    ##
variavel = "hello world"  # isso é uma variavel, tambem chamada de objeto!
#### daqui pra frente vamos chamar isso de objeto!

objeto_sring = "meu nome é arthur!"
objeto_sring2 = objeto_sring  # vai receber o conteudo daquele objeto

objeto_soma_strings = variavel + objeto_sring  # e se somasse com o objeto_string2?
#### fazer tambem um somando espaço
objeto_soma_strings_2 = "oi" + "meu" + "nome" + "é" + "Arthur"  # vai ficar sem " "


############################
## int, operacoes e float ##

objeto_int = 234
objeto_int_convertido_pra_string = str(objeto_int)

operacao_soma_int = objeto_int + objeto_int
operacao_soma_int_e_string = objeto_int + objeto_sring  # vai dar erro, string só se soma com str, int com int
#### criar um objeto int mas com " " e usar o int()

#### realizar tambem operacoes de -, *, / com string e int, pro estudante ver o resultado

objeto_float = 5.234
#### tambem realizar operacoes com o float
objeto_float_convertido_em_int = int(objeto_float)  # e converter int pra float?



############
##  bool  ##

objeto_boolean_true = True  # ou False
objeto_boolean_false = False

objeto_or = objeto_boolean_true or objeto_boolean_false
objeto_and = objeto_boolean_true and objeto_boolean_false
objeto_not_or = not(objeto_boolean_true or objeto_boolean_false)
#### e se a gente fizesse = not(objeto_or), nao daria na mesma?



############
##  dict  ##

objeto_dict = {"chave": "valor"}
objeto_dict_2 = {"chave_1": "valor_1", "chave_2": "valor_2"}
#### mostrar como fica quebrando a linha, mais facil de entender

valor_chave = objeto_dict.get('chave')
valor_chave_1 = objeto_dict.get('chave_1')

valor_chave_alt = objeto_dict['chave']
valor_chave_1_alt = objeto_dict['chave_1']
#### explicar porque isso acontece

keys = objeto_dict_2.keys()
values = objeto_dict_2.values()


############
##  list  ##
lista = [1, 2, 3, 4]
lista.append(5)

#### criar varias listas, e acessar os objetos dela, usando [0], [-1], e [:]


#############
### input ###
resultado = input("digite um numero")
resultado = int(resultado)
