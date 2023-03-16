# Exercicio 1.

peso = float(input("Digite o peso: "))
altura = float(input("Digite a altura: "))

def IMC(alt, peso):
  imc = peso / (alt * alt)
  return imc

if ((peso>0) and (altura>0)):
  if (IMC(altura, peso) <= 18.5):
    print("Abaixo do peso")
  elif (IMC(altura, peso) > 18.5 and IMC(altura, peso) <= 25):
    print("Peso normal")
  elif (IMC(altura, peso) > 25 and IMC(altura, peso) <= 30):
    print("Acima do peso")
  else:
    print("Obeso")
else:
  print("Entrada inválida!")

# Exercicio 2.
print("*"*45)
genero = input("\n (M) Masculino \n (F) Feminino \n (O) Outros \n Digite o gênero: ")
if (genero=="M" or genero=="F" or genero=="O"):
  print("*"*45)
  print("Sexo Válido!")
else:
  print("*"*45)
  print("Opção inválida")


# Exercicio 3.


# Exercicio 3.
numeros = []

while len(numeros)<3:
  numeroEntrada = int(input("Digite um numero: "))
  numeros.append(numeroEntrada)

numeros.sort(reverse=True)
print(numeros)

# # Exercicio 4.
Notas = []
iterador = 0
while iterador < 5:
  NotaFinal = float(input(f"Digite a nota 0{iterador+1}: "))
  Genero = input("Digite o Gênero [M], [F] ou [O]: ")
  print("*"*45)
  NotaIndividual = [Genero, NotaFinal]
  Notas.append(NotaIndividual)
  iterador = iterador+1

QntAlunosAprovados = 0
iterador2 = 0
for NotasGenero in Notas:
  if (Notas[iterador2][1]>=6):
    QntAlunosAprovados = QntAlunosAprovados + 1
  iterador2 = iterador2 + 1

qntAlunosAprovadosO = 0
qntAlunosAprovadosM = 0
qntAlunosAprovadosF = 0
iterador3 = 0
for NotasPorGenero in Notas:
  if (Notas[iterador3][0].upper()=='M' and Notas[iterador3][1]>=6):
    qntAlunosAprovadosM = qntAlunosAprovadosM + 1
  elif (Notas[iterador3][0].upper()=='F' and Notas[iterador3][1]>=6):
    qntAlunosAprovadosF = qntAlunosAprovadosF + 1
  elif  (Notas[iterador3][0].upper()=='O' and Notas[iterador3][1]>=6):
    qntAlunosAprovadosO = qntAlunosAprovadosO + 1
  iterador3 = iterador3 + 1

NotaSomada = 0
iterador4 = 0
for SomandoNotas in Notas:
  NotaSomada += Notas[iterador4][1]
  iterador4 += 1

print(f"\n\n  Alunos aprovados: {QntAlunosAprovados}")
print("*"*45)
print(f"\n Alunos [Outros] Aprovados: {qntAlunosAprovadosO}")
print("*"*45)
print(f"\n Alunos [Masculino] Aprovados: {qntAlunosAprovadosM}")
print("*"*45)
print(f"\n Alunos [Feminino] Aprovados: {qntAlunosAprovadosF}")
print("*"*45)
print(f"\n Média Final: {NotaSomada/5}")