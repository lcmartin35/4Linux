#!/usr/bin/python3
'''
ler o nome de um aluno
ler duas notasss e calcular  a media
mostrar a media do  aluno
'''
aluno =  input('Digite o nome : ')
nota1 =  int(input('Digite a Nota :'))
nota2 =  int(input('Digite a outra nota :'))
aluno =  aluno.title() 
# title()  deixa a primeira letra   maiscuula
# upper()  deixa todas as letras maisculas
# lower()  deixa todas as letras minusculas  
# strip()  retira os espaços em branco
# replace('a','@') altera o primeiro item pelo segundo dentro da string Ex:
aluno = aluno.replace('i','1' )


media = (nota1 + nota2) /2

if media >= 7:
    result = 'Aprovado'
elif media < 7 and media > 4:
    result = 'Recupercao'
else:
    result = 'Reprovado'

print('''
Aluno: {} 
Media: {}
Resultado: {}
         '''.format(aluno, media, result) )

    
