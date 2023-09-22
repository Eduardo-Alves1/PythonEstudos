def area (lar, comp):
    soma_area = lar * comp
    print( f"A ÁREA DO TERRENO {lar} X {comp} É DE {soma_area}m².")


print("CONTROLE DE TERRENO")
print("="* 20)

la = float(input("LARGURA (m): "))
cm = float(input("CO    MPRIMENTO (m): "))


area(la,cm)