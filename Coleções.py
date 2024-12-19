'''
Coleção de informações
'''
# idade1 = 30
# idade2 = 35
# idade3 = 27
# idade4 = 18

# print(idade1,idade2,idade3, idade4, sep='\n')

'''
Lista das coleções
'''
idades = [30,35,27,18] #Posições de cada informação é chamada normalmente de arrays.
         #1   2  3  4

print(type(idades)) # Mostra qual o tipo da informção (list, tuple, int, float) 
print(len(idades)) # Quantas informções possui (Conta a quantidade de itens)
print(idades) #Exibe todas as informações da lista

'''
Exibe para o usuario informação dentro da posição 1, 2 e 3. Verificando na lista indicada temos: 35,27,18
'''
print(idades[1])
print(idades[2])
print(idades[3])

'''
Toda lista pode ter os seus valores alterados, adicionar valores também é permitido
'''

idades.append(42) # Append() adiciona ao final da lista
idades.append(42) # Append() adiciona ao final da lista
print(idades)
idades.remove(42) #Vai remover o elemeto correspondente, porém como temos ele se repetindo 2x, ele removera apenas a sua primeira aparição, 1° posição que corresponde á informação
print(idades)
idades.append(27) #Exemplo de remoção da primeira aparição do número
idades.remove(27)
print(idades)

# idades.clear() #Remove todos os elementos da lista
print(idades)

if 42 in idades:
    idades.remove(42)
    print(idades)

'''
Podemos inserir um item na posição desejada usando a função insert()
'''

idades.insert(0, 20) #Adicionar elemento no loca desejado (insert)
print(idades)

'''
Podemos adicionar mais de 1 elemento usando append, porém não é recomendado, não é uma boa pratica
'''
idades1 = [20,39,19]
idades1.append([27, 19]) # Ele cria outra lista e coloca dentro de outra lista, tipagem incomum

for e in idades1:
    print(f'Recebi o elemento {e}')

'''
Uma boa pratica para inserir aqueles elemetos de forma que a lista se extenda é usando o metodo exted()
'''
idades2 = [20,39,19]
idades2.extend([27,19]) #O extend() vai interar em cada elemento da lista e adicionar apenas o elemento a medida que ele vai interando. 
print(idades2)

idades2_no_ano_que_vem = []
# for idade in idades2:
#     idades2_no_ano_que_vem.append(idade+1)
# print(idades2_no_ano_que_vem)

idades2_no_ano_que_vem = ([(idade+1) for idade in idades2]) # Esse for abreviado faz a mesma função que o for de cima, porém está abreviado.

print(idades2_no_ano_que_vem)

#List Comprehension
def proximo_ano(idade):
    return idade+1
idade_teste = [proximo_ano(idade) for idade in idades2 if idade > 21] #
print(idade_teste)
