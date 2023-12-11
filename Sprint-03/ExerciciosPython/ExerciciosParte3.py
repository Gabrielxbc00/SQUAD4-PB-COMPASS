# Questão 21

class Passaro:
    def voar(self):
        print("Voando...")

    def emitir_som(self):
        print("Passaro emitindo som...")

class Pato(Passaro):
    def emitir_som(self):
        super().emitir_som()
        print("Quack Quack")

class Pardal(Passaro):
    def emitir_som(self):
        super().emitir_som()
        print("Piu Piu")

pato = Pato()
print("Pato")
pato.voar()
pato.emitir_som()

print("\nPardal")
pardal = Pardal()
pardal.voar()
pardal.emitir_som()


# Questão 22

class Pessoa:
    def __init__(self, identificador):
        self.__nome = ""  
        self.id = identificador  

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

pessoa = Pessoa(0)
pessoa.nome = 'Fulano De Tal'
print(pessoa.nome)


# Questão 23

class Calculo:
    def somar(self, x, y):
        return x + y

    def subtrair(self, x, y):
        return x - y

x = 4
y = 5

calculo = Calculo()

resultado_soma = calculo.somar(x, y)
print(f"Somando: {x} + {y} = {resultado_soma}")

resultado_subtracao = calculo.subtrair(x, y)
print(f"Subtraindo: {x} - {y} = {resultado_subtracao}")


# Questão 24

class Ordenadora:
    def __init__(self, lista_baguncada):
        self.__lista_baguncada = lista_baguncada

    @property
    def listaBaguncada(self):
        return self.__lista_baguncada

    @listaBaguncada.setter
    def listaBaguncada(self, nova_lista):
        self.__lista_baguncada = nova_lista

    def ordenacaoCrescente(self):
        return sorted(self.listaBaguncada)

    def ordenacaoDecrescente(self):
        return sorted(self.listaBaguncada, reverse=True)

crescente = Ordenadora([3, 4, 2, 1, 5])
decrescente = Ordenadora([9, 7, 6, 8])

resultado_crescente = crescente.ordenacaoCrescente()
resultado_decrescente = decrescente.ordenacaoDecrescente()

print(resultado_crescente)
print(resultado_decrescente)


# Questão 25

class Aviao:
    def __init__(self, modelo, velocidade_maxima, capacidade):
        self.modelo = modelo
        self.velocidade_maxima = velocidade_maxima
        self.capacidade = capacidade
        self.cor = "Azul"

entradas = [
    {"modelo": "BOIENG456", "velocidade_maxima": 1500, "capacidade": 400},
    {"modelo": "Embraer Praetor 600", "velocidade_maxima": 863, "capacidade": 14},
    {"modelo": "Antonov An-2", "velocidade_maxima": 258, "capacidade": 12}
]

lista_avioes = []

for entrada in entradas:
    aviao = Aviao(entrada["modelo"], entrada["velocidade_maxima"], entrada["capacidade"])
    lista_avioes.append(aviao)

for aviao in lista_avioes:
    print(f"O avião de modelo {aviao.modelo} possui uma velocidade máxima de {aviao.velocidade_maxima} km/h, capacidade para {aviao.capacidade} passageiros e é da cor {aviao.cor}.")
