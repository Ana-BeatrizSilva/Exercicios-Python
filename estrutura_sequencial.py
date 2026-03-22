# 1. Mostrar mensagem "Olá, Mundo!":

print("Olá, Mundo!")

# 2. Mostrar número:

num = int(input("Informe um número: "))
print(f"O número informado foi {num}")

# 3. Soma de dois números:

num1 = int(input("Informe o primeiro número: "))
num2 = int(input("Informe o segundo número: "))
soma= num1 + num2
print(f"A soma entre {num1} e {num2} é: {soma}")

# 4. Média das notas:

nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))
nota3 = float(input("Informe a terceira nota: "))
nota4 = float(input("Informe a quarta nota: "))
media = (nota1+nota2+nota3+nota4)/4
print(f"A média das notas é: {media}")

# 5. Converter metros para centímetros:

metro = float(input("Informe o valor em metros: "))
cm = metro * 100
print(f"O valor em centímetros é: {cm}")

# 6. Área de um círculo:

raio = float(input("Informe o raio do círculo: "))
areaCirculo = 3.14 * (raio**2)
print(f"A área do círculo é: {areaCirculo}")

# 7. Área de um retângulo e seu dobro:

base = float(input("Informe a área da base: "))
altura = float(input("Informe a altura: "))
areaRetangulo = base * altura
dobroAreaRetangulo = areaRetangulo * 2
print(f"A área do retângulo é: {areaRetangulo}")
print(f"O dobro da área é: {dobroAreaRetangulo}")

# 8. Salário no mês:

salarioHora = float(input("Informe seu salário por hora: "))
horasMes = float(input("Informe a quantidade de horas trabahadas no mês: "))
salarioMes = salarioHora * horasMes
print(f"Seu salário no mês é : {salarioMes}")

# 9. Converter Fahrenheit para Celsius:

fah = float(input("Informe a temperatura em Fahrenheit: "))
cel = ((fah - 32)/9) * 5
print(f"A temperatura em graus Celsius é: {cel}")

# 10. Converter Celsius para Fahrenheit:

celsius = float(input("Informe a temperatura em Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"A temperatura em Fahrenheit é: {fahrenheit}")

# 11. Dois números inteiros e um real:

inteiro1 = int(input("Informe o primeiro número inteiro: "))
inteiro2 = int(input("Informe o segundo número inteiro: "))
real = float(input("Informe o número real: "))
operacao1 = (inteiro1 * 2)*(inteiro2/2)
operacao2 = (inteiro1 * 3)+real
operacao3 = real**3
print(operacao1)
print(operacao2)
print(operacao3)

# 12. Gigabytes para Megabytes:

giga = int(input("Informe o tamanho em Gigabytes: "))
mega = giga * 1024
print(f"O tamanho em Megabytes é: {mega}")

# 13. Gigabytes para Kylobytes: 

gigabytes = int(input("Informe o tamanho em Gigabytes: "))
kilo = gigabytes * 1024 * 1024
print(f"O tamanho em Kilobytes é: {kilo}")

# 14. João, um pescador, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas:

peso = float(input("Informe o peso dos peixes em kg: "))
excesso = max(0, peso - 50)
multa = excesso * 4
print(f"Peso: {peso} kg")
print(f"Excesso: {excesso} kg")
print(f"Multa: {multa} R$")

# 15. Calcular quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato:

salario_hora = float(input("Informe o salário por hora: "))
horas_trabalhadas = int(input("Informe o total de horas trabalhadas no mês: "))
salario_bruto = salario_hora * horas_trabalhadas

ir = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
total_descontos = ir + inss + sindicato
salario_liquido = salario_bruto - total_descontos

print(f"Salário bruto: {salario_bruto}")
print(f"Imposto de renda: {ir}")
print(f"INSS: {inss}")
print(f"Sindicato: {sindicato}")
print(f"Salário líquido: {salario_liquido}")

# 16. Informar o tamanho em metros de uma área a ser pintada. A cobertura é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.

import math 

area = float(input("Informe o tamanho da área em metros quadrados: "))
qtde_litros = area/6
latas = math.ceil(qtde_litros/18)
preco_total = latas * 80

print(f"Área: {area} metros quadrados")
print(f"Litros necessários: {qtde_litros}")
print(f"Latas necessárias: {latas}")
print(f"Preço total: {preco_total}")