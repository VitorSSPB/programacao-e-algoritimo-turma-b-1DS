cidade_a = 80000
cidade_b = 200000
anos = 0
while cidade_a <= cidade_b:
    cidade_a = cidade_a * 1.03
    cidade_b = cidade_b * 1.015
    anos += 1
print(f"A Cidade A ultrapassa a Cidade B em {anos} anos.")
print(f"Cidade A: {cidade_a:.0f} habitantes")
print(f"Cidade B: {cidade_b:.0f} habitantes")
