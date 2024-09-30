import os

# Limpar CMD:
def limpar():
    # Verifica o sistema operacional
    if os.name == 'nt':  # Windows
        os.system('cls')

# Tiers dos Oath's Comuns:
def Tiercomum():
    
    # Definindo Tiers e Cores
    tiers = {
        "1. Tier I": "\033[97mBranco",  # Branco
        "2. Tier II": "\033[92mVerde",  # Verde
        "3. Tier III": "\033[94mAzul",  # Azul
        "4. Tier IV": "\033[95mRoxo",   # Roxo
        "5. Tier V": "\033[90mPreto",   # Preto
    }
    
    # Resetando a cor para o terminal voltar à cor normal
    reset = "\033[0m"
    limpar()
    
    # Exibindo os Tiers
    print("📜 Níveis e cores dos Oaths 📜\n")
    for tier, color in tiers.items():
        print(f"{tier}{reset}: {color}{reset}")

# Tiers dos Oath's Lendários:
def Tierslenda():
    
    tierslend = {
        "1. Tier VI": "\033[38;5;214mLaranja", # Laranja
        "2. Tier VII": "\033[91mVermelho",     # Vermelho
        "3. Tier VIII": "\033[93mDourado",     # Dourado
    }
    
    # Resetando a cor para o terminal voltar à cor normal
    reset ="\033[0m"
    
    print("\n📜 Níveis e cores dos Oaths Lendarios 📜\n")
    for tier, color in tierslend.items():
        print(f"{tier}{reset}: {color}{reset}")