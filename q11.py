sa=float(input("digite seu salario atual"))
salario_atual = 0.0
des = 0.0
percentual_de_aumento = 0.0
if sa <=280:
    percentual_de_aumento=20
elif sa <=750:
    percentual_de_aumento=15
elif sa <=1500:
    percentual_de_aumento=10
else:
    percentual_de_aumento=5

des=sa*(percentual_de_aumento/100)
salario_atual=sa+des
print(f"seu salario antes do reajuste era de R$ {sa:.2f}")
print(f"seu salario foi aumentado em {percentual_de_aumento}%")
print(f"seu salario foi aumentado em R$ {des:.2f}")
print(f"seu salario atual e de R$ {sa:.2f}")


