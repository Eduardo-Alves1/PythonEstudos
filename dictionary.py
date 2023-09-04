#DICIONÁRIOS

# Dicionários são estruturas que compreendem um conjunto de pares: chave e valor. 
# Cada chave individual possui um valor associado. Esse tipo de associação se dá o nome de coleção associativa desordenada.
# Assim como as listas, os dicionários são mutáveis. 
# O conteúdo de um dicionário é delimitado por chaves e os elementos são separados por vírgula.

dicionario_1 = {"Idade": 30, "Nome": "Eduardo Alves", "Peso": 106}

#ACESSANDO UM VALOR PELA CHAVE
idadade = dicionario_1["Idade"]
print(idadade)

#UTILIZANDO GET

idade2 = dicionario_1.get("")