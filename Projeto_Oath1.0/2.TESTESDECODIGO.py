# Importações:
import random
import os
from Probabilidades import valores, peso, valoreslend, pesolend, limite_maxatri, limite_minatri
from Dados_importantes import vantagens, estilos, tipos
from Regras_dados import Tiercomum, Tierslenda
from Gerar_Nomes import Gerar_Nomes_Random

def limpar():
    if os.name == 'nt':  # Windows
        os.system('cls')

def Gerar_Oath():
    
    # Variaveis:
    limite = 0
    tier = 0
    atri = {'Força': 0, 'Destreza': 0, 'Poder Mágico': 0, 'Durabilidade': 0, 'Foco': 0}
    maxatri = {'Força': 0, 'Destreza': 0, 'Poder Mágico': 0, 'Durabilidade': 0, 'Foco': 0}
    
    # Converte as chaves dos dicionários em LISTA para sorteio com random.choice:
    vant = list(vantagens.keys())
    est = list(estilos.keys())
    
    # Amostragem:
    limpar()
    print("=" * 50)
    print("🔮 Bem-vindo ao Gerador de Oaths! 🔮")
    print("=" * 50)
    print("\n")
    Tiercomum()
    
    # Preencer Requisitos:
    tier = int(input("\nQual o tier do oath que você quer gerar? Ex.: 1 seria Branco --> "))
    limite  = int(input("Quantos Oath's você quer gerar? --> "))
    
    # Inicio:
    for comeco in range(limite):
        
        # Sorteia uma vantagem, uma natureza e um tipo para o Oath:
        vantsort = random.choice(vant)
        estsort = random.choice(est)
        tiposort = random.choice(tipos)
        
        # Sorteia se é ou não é Shiny (em, hãm? é ou não é?):
        if random.random() < 0.05:
            shiny = 1
        else:
            shiny = 0

        # Sorteia tipos adicionais com 40% de chance:
        if random.random() < 0.4:
            restypes = [tipo for tipo in tipos if tipo != tiposort]
            # Corrigindo para que ele não escolha um tipo que o Oath já tenha:
            sectipos = random.choice(restypes) if restypes else None 
        # Caso o sorteio nao der os 40% ele aderir valor Nulo a sectipos:
        else:
            sectipos = None
            
        # Definindo os atributos maximos de forma aleatoria do Tier do Oath escolhido:
        while True:
            soma = 0
            for attr in maxatri.keys():
                dado = random.choices(valores[tier], peso[tier])[0]
                maxatri[attr] = dado
                soma += maxatri[attr]
        
            if limite_minatri[tier] <= soma <= limite_maxatri[tier]:
                break
            
        # Distribuição dos Atributos, com tratamento para determinados valores:
        for attr in maxatri:
            if maxatri[attr] == 4:
                atri[attr] = 2
            elif maxatri[attr] == 7:
                atri[attr] = 3
            elif maxatri[attr] == 8:
                atri[attr] = 4
            elif maxatri[attr] == 9:
                atri[attr] = 5
            else:
                atri[attr] = max(maxatri[attr] - 3, 1)

        # Define os Pv's baseados no Tier:
        if tier == 1:
            Pv = random.randint(2, 3)
        elif tier == 2:
            Pv = random.randint(3, 4)
        elif tier == 3:
            Pv = random.randint(3, 4)
        elif tier == 4:
            Pv = random.randint(4, 5)
        else:
            Pv = random.randint(5, 6)
        
        # Define os Pontos de Vida totais do Oath:
        Pvtotal = Pv + atri['Durabilidade']

        # Exibição do Oath:
        print("=" * 50)
        print(f"🌟 Resultado da Geração do Oath {comeco+1} 🌟")
        print("=" * 50)
        print(F"🌟Nome: {Gerar_Nomes_Random()}🌟")
        print(f"🎯 Seu TIER foi: {tier}")
        print("=" * 50)
        print("✨ Atributos do Oath:")
        print("=" * 50)
        
        # Caso o Oath sejá shiny:
        if shiny == 1:
            print("🌟✨🌟✨ Seu Oath é um Shiny 🌟✨🌟✨")
            print("=" * 50)
            Pvtotal+=1
        
        # Demonstra os atributos dos Oath's em bolinhas:
        for nm in maxatri:
            distribuido = '•' * atri[nm]
            distribuir = 'o' * (maxatri[nm] - atri[nm]) 
            print(f"🔹 {nm}: {distribuido}{distribuir}")

        # Demonstra os dados restantes (Pv's, Tipos, Natureza e Vantagens):
        if shiny == 0:
            print(F"❤️ Pontos de Vida ❤️ : {Pvtotal} = {Pv} + {atri['Durabilidade']}")
        else: # Caso seja shiny recebe esses dados adicionais:
            print(F"❤️ Pontos de Vida ❤️ : {Pvtotal} = {Pv} + {atri['Durabilidade']} + 1 (Shinys recebem este adicional!)")
        
        print(F"Def. Fisica 🛡️🛡️ : {atri['Durabilidade']}")
        print(F"Def. Mágica ✨🛡️ : {atri['Foco']}")
        
        print("🎯 Vantagens 🎯")
        print(F"{vantsort}: {vantagens[vantsort]}")
        
        print("🔥💧🌿Tipo🌿💧🔥")
        print(F"Tipagem: {tiposort}", end=" ")
        if sectipos:
            print(F" e {sectipos}")
        else:
            print()
        
        print("⚔️  Estilo de Combate  ⚔️")
        print(F"{estsort}: {estilos[estsort]}")
        print("\n" + "=" * 50 + "\n")
        
        #Garante que o shiny caso seja sorteado resete seu resultado para o próximo sorteio:
        shiny = 0

while True:
    Gerar_Oath()
    i = input(">>")
    if i == '1':
        break