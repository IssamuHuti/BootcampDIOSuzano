# metodos manipulação de string

curso = 'python programa'

print(curso.upper())
print(curso.lower())
print(curso.title())
print()

curso2 = '    python programa    '

print(curso2.strip())
print(curso2.lstrip())
print(curso2.rstrip())
print()


curso3 = 'python'

print(curso3.center(10))
print(curso3.center(10, '#'))
print('.'.join(curso3)) # pode ser usada para todos os elementos iteráveis, como string e lista
print()


# interporação

nome = 'Lucas'
idade = 27
profissao = 'programador'
linguagem = 'python'

# old style %
print('ola, me chamo %s. Eu tenho %d anos de idade, trabalho com %s e estou matriculado no curso de %s.' % (nome, idade, profissao, linguagem))
print()
# %s = string; %d = idade

# metodo format {}
print('ola, me chamo {}. Eu tenho {} anos de idade, trabalho com {} e estou matriculado no curso de {}.'.format(nome, idade, profissao, linguagem))
print()

# f-string
print(f'ola, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho com {profissao} e estou matriculado no curso de {linguagem}.')

PI = 3.14159

print(f'Valor do PI = {PI:.2f}')
print(f'Valor do PI = {PI:10.2f}')


# fatiamento de strings
nome_completo = 'Lucas Issamu Morino Yamahuti'

print(nome_completo[0])
print(nome_completo[:5])
print(nome_completo[6:])
print(nome_completo[6:20])
print(nome_completo[6:20:3])
print(nome_completo[:])
print(nome_completo[::-1])
print()

mensagem = f'''
    Olá, meu nome é {nome_completo},
estou aprendendo python agora
'''

print(mensagem)

print('''
************** MENU **************

1 - Depositar
2 - Sacar
3 - Sair

**********************************
'''
)