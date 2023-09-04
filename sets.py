# SETS

# Os sets são mutáveis o que permite alterar, excluir ou adicionar itens, porém, seus itens devem ser imutáveis — como string, int ou tuplas.
# Os sets possuem métodos para operações matemáticas como união, interseção, diferença e diferença assimétrica.
# Na imagem a seguir podemos ver o comportamento de cada uma dessas operações e no código de exemplo apresento um pouco desses recursos.

frutas_1 = {"Banana", "Uva", "Jaca", "Macan"}
frutas_2 = {"Pera", "Uva", "Ameixa", "Macan"}

print(frutas_1 | frutas_2)  # UNIÃO - Juntando os dois Sets sem que haja repetições

# Interseção - Frutas em comum nos dois SETS"
print(frutas_1 & frutas_2)

print(frutas_1 - frutas_2)  # Diferença - o que tem na FRUTA_1 que não tem em FRUTA_2


frutas_2.add("Acerola") # É possivel adiciona e remover intens
print("Foi adicionado a fruta ",frutas_2)