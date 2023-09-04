# LISTA

# Esse tipo de coleção é uma estrutura de dados
# indexados e armazenados em sequência, onde cada elemento possui uma
#  posição que é identificada por um índice. O primeiro elemento à esquerda
# da lista é o índice 0 e em cada elemento da sequência o valor do índice é
# incrementado (+1). Ainda é possível realizar a indexação dos itens por valores negativos,
# nesse caso a indexação ocorre da direita para esquerda com decremento (-1).
# Na imagem a seguir é apresentado um exemplo de lista com a indexação positiva e negativa.

# Uma lista no Python pode armazenar qualquer tipo de dado primitivo (string, int, float, etc.).
# Também é possível criar listas dentro de listas — os populares nested list.

lista_python = ["Eduardo", "Thais", "Daniel", "Melissa"]
print(lista_python)

lista_python[0] = "Eduardo Alves" #Acessando o valor da lista no indice 0 e alterando o valor
print(lista_python)

lista_python.append("Duck") #Adicionadno um novo valor a lista no final
print(lista_python)

lista_python.remove("Duck") # Removendo um valor da lista utilizando o metodo REMOVE, podemos usar tam o metodo POP com este passando o indice do valor a ser removido
print(lista_python)