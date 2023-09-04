
# nome = "Eduardo"

# def funcao1():
#     print(nome)
    

# # NÃO PE POSSIVEL ALTERAR UMA VARIAVEL DE DENTRO DE UMA FUNÇÃO    
# def fun2():
   
#     nome = "Eduardo Alves"
#     print(nome)
# funcao1()
# fun2()
# print(nome)

def soma(num1, num2):
    resultado = num1 + num2
    return resultado

num1 = int(input("Digite um numero "))
num2 = int(input("Digite outro número"))

resultado_soma = soma(num1,num2)
print(resultado_soma)
