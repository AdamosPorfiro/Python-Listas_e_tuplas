'''Objetos próprios (classes)'''

class Conta_Corrente:
    
    def __init__(self,codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self,valor):
        self._saldo += valor
    
    def __str__(self):
        return f'[>>> Código: {self._codigo} | Saldo R${self._saldo} <<<]'
    
    @staticmethod
    def deposita_para_todas_as_contas(contas):
        for conta in contas:
            conta.deposita(100)

conta_do_adamos = Conta_Corrente(1)
conta_do_adamos.deposita(500)
conta_do_adamos.deposita(100)

conta_dani = Conta_Corrente(42)
conta_dani.deposita(1000)

contas = [conta_do_adamos, conta_dani]

# contas[2].desposita(300) # - Mutabilidade do objeto
# print(contas[0])
print(contas[0], contas[1], sep='\n')
Conta_Corrente.deposita_para_todas_as_contas(contas)
print(contas[0], contas[1], sep='\n')

contas.insert(0,76) # - Multabilidade
print(contas[0], contas[1], contas[2], sep='\n')

Conta_Corrente.deposita_para_todas_as_contas(contas)
print(contas[0], contas[1], contas[2], sep='\n')