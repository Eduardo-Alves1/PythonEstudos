import pandas as pd 

lista_motorista = pd.read_excel("MOTORISTAS_PROCISA.xlsx")

#print(lista_motorista)
tabela = []
for motorista in lista_motorista.index:
        nome = lista_motorista.loc[motorista,"primeiro nome"]
        matricula = lista_motorista.loc[motorista, "matricula"]
        
        print(nome,"-",matricula)