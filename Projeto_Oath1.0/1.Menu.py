#Aqui é a area principal do codigo, onde terá apenas as importações para chamar cada
#função necessaria.

#Importando as funções:
from Gerar_Oath import Gerar_Oath, Gerar_Oath_Random, Gerar_Lend, Gerar_Lend_Random, limpar #1º Opção
from Regras_dados import Tierslenda, Tiercomum #3º Opção
from Dados_importantes import exibir_ficha_jogador, ficha_jogadorAT, ficha_jogadorMX #3º Opção
from Gerar_Nomes import Gerar_Nomes_Random
#from Abrir_Boosters import

#Chamando as variaveis:
esc = 0

while True: # Loop Infinito:
    
    #Interação com úsuario:
    print("===================================")
    print("        🌟 Menu Principal 🌟      ")
    print("===================================")
    print("1. ✨ Gerar Oaths Aleatórios ✨")
    print("2. 🎴 Abrir Boosters 🎴")
    print("3. 📜 Regras 📜")
    print("4. ❌ Sair ❌ ")
    print("===================================")

    esc = int(input("Escolha a opção desejada: "))
    # Limpar tela após escolha:
    limpar()

    # Seguimento da escolha do úsuario:
    if esc == 1:
        
        while True: # Loop infinito:
            
            # Menu de escolhas:
            print("=" * 30)
            print("✨ Gostaria de gerar Oath's: ✨")
            print("=" * 30)
            print("1. 🏆🏆 Escolhendo Comuns")
            print("2. 🏆🎲 Comuns Aleatórios")
            print("3. 🌟🌟 Lendários")
            print("4. 🌟🎲 Lendários Aleatórios")
            print("=" * 30)
            esc = int(input("Escolha uma opção >>> "))
                
            # Seguimento da escolha do úsuario para geração:
            if esc == 1:
                Gerar_Oath()
                # Faz uma pausa no programa e depois limpa o CMD e volta ao menu principal:
                input("Precione ENTER para Voltar ao Menu ...")
                limpar()
                break
            elif esc == 2:
                Gerar_Oath_Random()
                # Faz uma pausa no programa e depois limpa o CMD e volta ao menu principal:
                input("Precione ENTER para Voltar ao Menu ...")
                limpar()
                break
            elif esc == 3:
                Gerar_Lend()
                # Faz uma pausa no programa e depois limpa o CMD e volta ao menu principal:
                input("Precione ENTER para Voltar ao Menu ...")
                limpar()
                break
            elif esc == 4:
                Gerar_Lend_Random()
                # Faz uma pausa no programa e depois limpa o CMD e volta ao menu principal:
                input("Precione ENTER para Voltar ao Menu ...")
                limpar()
                break
            else:
                print("Opção incorreta digite novamente!")         
    elif esc == 2:
        print()
    elif esc == 3:
        Tiercomum()
        print("="*50)
        Tierslenda()
        print("="*50)
        exibir_ficha_jogador(ficha_jogadorMX, ficha_jogadorAT)
        # Faz uma pausa no programa e depois limpa o CMD e volta ao menu principal:
        input("Precione ENTER para Voltar ao Menu ...")
        limpar()
    elif esc == 4:
        print("Fechando")
        exit()
    elif esc == 5: # Teste de Geração de nomes: NÃO CONSTA NO MENU.
        esc = int(input(">>> "))
        cont=0
        for i in range(esc):
            cont+=1
            print(F"{cont}: {Gerar_Nomes_Random()}")
        input("Precione Enter para voltar ao menu ...")
        limpar()