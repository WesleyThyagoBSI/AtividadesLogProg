
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados (ok) que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros; (ok)
# comprar apenas galões de 3,6 litros; (ok)
# misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

# entrada de dados
area_pintada = float(input("Digite a área a ser pintada (m²): "))
# declaracao das variaveis
quantidade_de_tinta = (area_pintada / 6)*1.1
quantidade_de_latas = quantidade_de_tinta / 18
quantidade_de_galoes = quantidade_de_tinta / 3.6
# declaração de um dicionário para armazenar os desperdicios de tinta em litros
desperdicios = {}

print(f"A quantidade de tinta é: {round(quantidade_de_tinta,2)} litros")

#calcular o desperdicio comprando só quantidade_de_latas
if(quantidade_de_latas>int(quantidade_de_latas)): # ou seja, se a quantidade necessaria de latas para pintar a parede for maior q a lata cheia
  desperdicioLata = (round(quantidade_de_latas+0.5)-quantidade_de_latas)*18
  desperdicios['DesperdicioLata'] = desperdicioLata
else:
  desperdicios['DesperdicioLata'] = 0

#calcular o desperdicio comprando só quantidade_de_galoes
if(quantidade_de_galoes>int(quantidade_de_galoes)):
  desperdicioGalao = (round(quantidade_de_galoes+0.5)-quantidade_de_galoes)*3.6
  desperdicios['DesperdicioGalao'] = desperdicioGalao
else:
  desperdicios['DesperdicioGalao'] = 0

if(quantidade_de_latas>int(quantidade_de_latas)):
  sobra_lata = (quantidade_de_latas-int(quantidade_de_latas))*18
  quantidade_mistura_galoes = round((sobra_lata/3.6)+0.5)
  soma_litros_mistura = int(quantidade_de_latas)*18+(quantidade_mistura_galoes*3.6)
  desperdicio_misturaGaloesLatas = soma_litros_mistura-quantidade_de_tinta
  desperdicios['DesperdicioMistura'] = desperdicio_misturaGaloesLatas
else:
  desperdicios['DesperdicioMistura'] = 0

for tipoDesperdicio, qntDesperdicada in desperdicios.items():
  if(tipoDesperdicio=='DesperdicioLata'):
    print(f"Comprando {round(quantidade_de_latas+0.5)} latas custando R$ {round(round(quantidade_de_latas+0.5)*80,2)} gerando um desperdício de {round(qntDesperdicada,2)} litros")
  elif(tipoDesperdicio=='DesperdicioGalao'):
    print(f"Comprando {round(quantidade_de_galoes+0.5)} galões custando R$ {round(round(quantidade_de_galoes+0.5)*25,2)} gerando um desperdício de {round(qntDesperdicada,2)} litros")
  elif(tipoDesperdicio== 'DesperdicioMistura'):
    print(f"Comprando {int(quantidade_de_latas)} latas e {quantidade_mistura_galoes} galões custando R$ {(int(quantidade_de_latas)*80)+(quantidade_mistura_galoes*25)} gerando um desperdício de {round(qntDesperdicada,2)} litros")
  
  