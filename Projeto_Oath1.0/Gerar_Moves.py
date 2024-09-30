# Gerar movimentos para combate:

# Importações:
import random
from Dados_importantes import moveseffect, efnega, efposi, tipos
from Probabilidades import pesomoves, valoresmoves

def Gerar_Move_Atk_Random():
    
    # Variaveis:
    power = 0
    estilo = ['Fisico', 'Mágico']
    alcance = ['Corpo-a-Corpo', 'À Distância'] 
    
    # Fisicos:
    accfis = ['Força','Foco','Destreza']
    danfis = ['Força','Durabilidade']
    
    # Mágicos:
    accmag = ['Poder Mágico','Foco', 'Destreza']
    danmag = ['Poder Mágico', 'Mana', 'Foco']
    
    # Gerando dados:
    power = random.choices(valoresmoves, weights=pesomoves)[0]
    sortestilo = random.choice(estilo)
    tipsort = random.choice(tipos)
    alcsort = random.choice(alcance)
    
    # Dados Fisicos:
    accfisort = random.choice(accfis)
    danfisort = random.choice(danfis)
    
    # Dados Mágicos:
    accmagsort = random.choice(accmag)
    danmagsort = random.choice(danmag)
    
    # Definindo o tipo do Move:
    if sortestilo == 'Fisico':
        if power in (5,6):
            sortneg = random.choice(efnega)
        print(F"Tipo: {tipsort} | Power: {power} | if sort: {alcsort}")
            
    
'''
________________________________________________

nome do move / Poder: 0
________________________________________________
Precisão: Força, Destreza, Foco, Poder Mágico
Dano: Força, Durabilidade, Poder Mágico
Efeito Adicional: 
    Positivo:
    Negativo:
________________________________________________ 
'''
