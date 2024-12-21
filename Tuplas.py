'''
Tuplas são inicializadas com parenteses ('5', 'adamos'), elas armazenam valores diferentes e são imutaveis,tuplas não utilizam o append, como em listas.
'''

Conta_Adamos = (31, 1000) # -São imutaveis, guarda variações de valores.
Biriba = (25, 'Biriba', 1852) # -Errado

def deposita(conta): # -Separando o comportamento dos dados (Modelo funcional)
    novo_saldo = conta[1] + 100
    codigo = conta[0]
    return (codigo, novo_saldo)

print(deposita(Conta_Adamos))