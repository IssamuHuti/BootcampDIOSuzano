frutas = ['maçã', 'laranja', 'pera']

letras = list('python')

numeros = list(range(10))

print(frutas)
print(frutas[0])
print(letras)
print(letras[-1])
print(numeros)

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matriz[0][0])
print(matriz[1][2])
print(matriz[2][2])

# fatiamento
print(letras[2:])
print(letras[:2])
print(letras[1:3])
print(letras[0:3:2])
print(letras[::])
print(letras[::-1])

carros = ['gol', 'clio', 'uno', 'onix']

for carro in carros:
    print(carro)

for indice, carro in enumerate(carros):
    print(f'{indice+1}: {carro}')

pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)

lista = []
lista.append(1)
lista.append('lista')
lista.append([1, 2, 3])

print(lista)
# lista.clear() apaga todos os itens dentro da lista

l2 = lista.copy() # cria copia, assim a lista original não vai ser afetada

print(l2)

print(lista.count('valor')) # informa quantas vezes o 'valor' foi informado dentro da lista

lista.extend(carros)
print(lista)

print(lista.index('gol')) # informa a posição do valor dentro da lista

print(lista.pop()) # apaga o ultimo item da lista
print(lista)

print(lista.pop(2)) # apaga o item da lista com o indice informado
print(lista)

print(lista.remove('clio')) # remove da lista o valor informado
print(lista)


lista2 = ['python', 'java', 'js', 'ruby', 'c#', 'html', 'angular']

print(sorted(lista2))
print(sorted(lista2, reverse=True))
print(sorted(lista2, key=lambda x: len(x)))
print(sorted(lista2, key=lambda x: len(x), reverse=True))

print(len(lista2))

# tuplas
# são imutaveis
# tuple()
# utiliza a mesma lógica das listas para manupulação


# conjuntos ordemandos
# ela é informada entre chaves {}
# a função set converte listas, tuplas e strings em conjunto
# não repete os valores

lista3 = [1, 2, 3, 1, 2, 3, 4]
print(set(lista3))

print(set('abacaxi'))
print(('palio', 'gol', 'hb20', 'argo', 'gol', 'uno', 'palio'))

conjuntoA = {1, 2, 3}
conjuntoB = {3, 4, 5, 6, 7, 8}
conjuntoC = (4, 5, 6)

print(conjuntoA.union(conjuntoB))
print(conjuntoA.intersection(conjuntoB))
print(conjuntoA.difference(conjuntoB))
print(conjuntoB.difference(conjuntoA))
print(conjuntoB.symmetric_difference(conjuntoA))
print(conjuntoB.issuperset(conjuntoC))
print(conjuntoB.issuperset(conjuntoA))
print(conjuntoB.isdisjoint(conjuntoA))
print(conjuntoA.isdisjoint(conjuntoC))

exemplo1 = conjuntoA.add(0)
exemplo2 = conjuntoA.add(2)

print(exemplo1)
print(exemplo2)

# conjuntoA.clear() = apaga as informações contitdas no conjuntoA
# conjuntoA.copy() = copia um conjunto

descarte = conjuntoB.discard(6)
print(descarte)

# .pop() retira o primeiro item do conjunto
# .remove() retira do conjunto o item selecionado


# conjuntos não-ordenados (dicionário)
# informa chave e valor
# as chaves são imutáveis e não podem repetir

pessoa = {'nome': 'lucas', 'idade': 27}
pessoa2 = dict(nome='ana', idade=30)
pessoa['telefone'] = '1234-5678'

print(pessoa)
print(pessoa2)
print(pessoa['nome'])

pessoa['nome'] = 'maria'
print(pessoa)

contatos = {
    'contato1@contato.com.br': {'nome': 'Joao', 'telefone': '99999-9999'},
    'contato2@contato.com.br': {'nome': 'Maria', 'telefone': '99999-9998'},
    'contato3@contato.com.br': {'nome': 'Pedro', 'telefone': '99999-9997'},
    'contato4@contato.com.br': {'nome': 'Carol', 'telefone': '99999-9996'},
}

print(contatos['contato1@contato.com.br']['nome'])

for chave, valor in contatos.items():
    print(chave, valor)

# dict.fromkeys(['nome', 'telefone']) = cria um dicionário vazio
# dict.fromkeys(['nome', 'telefone'], 'vazio') = cria um dicionário com o valor de cada uma das chaves como 'vazio'


# contatos['chaves'] # se informar valor de uma chave inexistente, informa KeyError
print(contatos.get('chaves', {})) # procura dentro do dicionário se possui alguma chave com o mesmo nome da chave informada, se não retorna um valor predefinido 
print(contatos.get('contato4@contato.com.br', {}))

# dict.items() = retorna o valor das chaves e seus valores
# dict.keys() = retorna o valor das chaves
# dict.pop(chave_a_excluir, 'valor_se_chave_nao_existir')
# dict.popitem() = apaga o ultimo iten dentro do dicionário
# dict.setdefault('chave', 'valor') = se existir a chave, retorna o valor contitudo na chave sem alteração, porém se a chave não existir, cria a chave e informa o valor informado
# dict.update('chave', 'valor') = permite fazer a atualização do dicionário com novo dicionário, se a chave informado existir, só vai atualizar o valor, mas se não existir a chave, atualiza o dicionário com nova chave e novo valor
# dict.values() = retorna todos os valores dentro do dicionário

resultado = 'contato3@contato.com.br' in contatos
print(resultado)

resultado2 = 'teste@teste.com.br' in contatos
print(resultado2)

del contatos['contato2@contato.com.br']
del contatos['contato1@contato.com.br']['telefone']
print(contatos)