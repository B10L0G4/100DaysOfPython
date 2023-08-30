# 'Day 2'
# calculadora de massa corporal

altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))

bmc = peso // altura ** 2

print(round(bmc))
