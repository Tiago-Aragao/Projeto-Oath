# Criar logica para evolução dos Oath's:

# Importações:
import random
from Probabilidades import valoresevo, pesoevo
from Gerar_Oath import Gerar_Oath, Gerar_Oath_Random
 
# Ao passar uma função como parâmetro para evo_oath, quando
# chamamos evo_oath com Gerar_Oath ou Gerar_Oath_Random,
# a função escolhida será executada. O tier retornado por
# essa função será usado pelo evo_oath para determinar
# como será a evolução do oath.

def evo_oath(funcao):
    
    # Variaveis:
    tier = funcao() # Essa funcao executará o Gerar_Oath ou Gerar_Oath_Random que será passado como parametro.
    numevo = random.choices(valoresevo, weights=pesoevo)
    tempoevo = {"Rapido": "5 Vitórias.", "Médio": "15 Vitórias.", "Longo": "45 Vitórias."}
    atri = {'Força': 0, 'Destreza': 0, 'Poder Mágico': 0, 'Durabilidade': 0, 'Foco': 0}
    
    # Inicio da lógica:
    
    