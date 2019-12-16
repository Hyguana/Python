# Este script vamos criar um programa em que a pessoa insere seu ano de nascimento e receberá quantos anos fará no ano atual

print('Olá, Tudo bem ?')
name = input('Poderia inserir seu Nome?: ')
print('Prazer ',name,'.')
# Para definir uma variável como int Caso ela esteja dando erro tem que se usar esta estrutura
# b = int(input('descritivo para ser exibido na tela'))
b = int(input('Agora poderia por favor inserir o ano de seu nascimento (Ex: 1989): '))
#Para receber a data e hora do computador  foi utilizado a função datetime
from datetime import date
# Criada uma variavel para guardar toda a informação
data_atual = date.today()
# para separar a informação que queira da função datetime utilize .year ou a qure preferir
# para saber se está recebendo coloqe isto sem o comando de comentário print(data_atual.year)
# Aqui será uma variavel recebendo o cáculo
age = (data_atual.year - b)
# mostrando o resultado 
print('Então neste ano tu terás ',age,' anos de idade. Parabéns uma boa idade.')
