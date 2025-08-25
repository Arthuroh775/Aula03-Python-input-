# 2-Criar um programa em Python que calcule a idade de uma pessoa com base no ano de nascimento e no ano atual.
# Solicite ao usuário que digite seu ano de nascimento.


# Solicite ao usuário que digite o ano atual.


# Calcule a idade da pessoa.


# Exiba a idade no formato: "Você tem XX anos."

n1 = int (input(' Em qual ano você nasceu ? '))
n2 = int (input('Qual ano estamos : '))

age = n2 - n1 

print(f'Se você nasceu em {n1} , então você tem {age} anos !')

