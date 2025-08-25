# 1-O usuário deve digitar dois número e exibir usando o input:
# -A soma
# -A subtração
# -A multiplicação
# -A divisão

# Exemplo de execução:
# Digite o primeiro número: 8
# Digite o segundo número: 2

# Soma: 10
# Subtração: 6
# Multiplicação: 16
# Divisão: 4.0

# -Use float(input()) para aceitar números decimais.

n1 = float(input('Escolha um número: '))
n2 = float(input('Escolha o segundo número : '))

soma = int(n1 + n2 )
sub = int(n1 - n2 )
mult = int (n1 * n2 )
divi = int (n1 / n2 )
poot = int (n1 ** n2) 

print (f'Vocé escolheu os números {n1} e {n2}')
print('vamos fazer cada operação com eles : ')
print('='* 30)
print(f"{n1} + {n2} = {soma}")
print(f"{n1} - {n2} = {sub}")
print(f"{n1} X {n2} = {mult}")
print(f"{n1} / {n2} = {divi}")
print(f"{n1} ** {n2} = {poot}")