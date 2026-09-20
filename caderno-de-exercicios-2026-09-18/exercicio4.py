cotacao = 5.20
reais = float(input("Digite o valor em reais (R$): "))
dolares = reais / cotacao
print(f"Com R$ {reais:.2f} você pode comprar US$ {dolares:.2f}")
