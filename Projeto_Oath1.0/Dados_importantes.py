#Vantagens, Estilos e Tipos (por enquanto):

# Vantagens:
vantagens = {
    'Analisys': 'Se este Oath tiver uma iniciativa inferior à do seu alvo, adicione 1 dado a todas os suas jogadas de Dano.',
    'Anger Point': 'Se um inimigo conseguir um Acerto Crítico neste Oath, aumente 3 Pontos no seu Atributo de Força.',
    'Aura Spell': 'Aumente 1 ponto no Poder Mágico de todos os Oaths Aliados dentro do Alcance. Os Oaths Aliados recebem 1 Dado Extra em todas as suas jogadas de dano de habilidades mágicas.',
    'Battle Armor': 'Se um oponente acertar um golpe crítico neste Oath, ele não receberá nenhum dado de bônus por isso.',
    'Beast Boost': 'Se um oponente desmaiar devido a um ataque causado por este Oath, aumente 1 ponto em seu atributo com maior limite. Até 3 pontos podem ser aumentados dessa forma. O Beast Boost não pode ser trocado ou copiado.',
    'Berserker': 'Quando os Pontos de Vida deste Oath estiverem na metade ou menos, aumente seu atributo de Força ou Poder Mágico em 1, a sua escolha.',
    'Big Defense': 'Este Oath não pode ter sua Defesa reduzida.',
    'Bulletproof': 'Reduza em 1 todo dano de Ataques Especiais e Ataques Físicos à Distância feitos a este Oath.',
    'Clear Body': 'Outros Oaths não podem aumentar ou diminuir os atributos deste Oath. Este Oath ainda pode aumentar ou diminuir seus próprios atributos.',
    'Color Change': 'Quando este Oath recebe dano, ele mudará temporariamente seu tipo para corresponder ao tipo do golpe que o atingiu. O efeito termina se o Oath for removido da batalha.',
    'Cotton Down': 'Se este Oath for atingido por um Ataque Físico de Curto Alcance, reduza a velocidade de todos os Oaths próximos a ele.',
    'Competitive': 'A primeira vez que este Oath tiver um atributo reduzido por um oponente durante uma batalha, aumente 2 pontos na Força ou Poder Mágico.',
    'Compund Eyes': 'Este Oath recebe 2 Dados de Bônus nas jogadas de precisão de qualquer golpe com Precisão Reduzida.',
    'Contrary': 'Se algo diminuiria um atributo deste Oath, aumente-o em vez disso. Se algo aumentaria um atributo deste Oath, diminua-o em vez disso.',
    'Corrosion': 'Ignore qualquer imunidade que o oponente tenha a dano do tipo Veneno e/ou a ser afetado pelos status ENVENENADO(Condição) e INTOXICADO(Condição).',
    'Chlorophyll': 'Se o Clima Ensolarado estiver em efeito, aumente em 2 pontos o Atributo de Destreza deste Oath.',
    'Cursed Body': 'Quando este Oath recebe dano de um golpe, role 3 Dados de Chance para DESABILITAR(Status) esse golpe. Apenas um golpe pode ser desabilitado dessa forma.',
    'Cute Charm': 'Se um oponente atingir este Oath com um ataque físico não à distância, role 3 Dados de Chance para fazer o oponente se APAIXONAR(Status).',
    'Dark Aura': 'Este Oath é imune a danos do tipo Dark, além disso, adicione 1 dado a todas os suas jogadas de Dano com golpes do tipo Dark.',
    'Dauntless Shield': 'Quando este Oath entra em batalha, aumente 2 pontos em sua Defesa.',
    'Dazzling': 'Os oponentes não podem usar Golpes de Prioridade contra este Oath.',
    'Defiant': 'A primeira vez que este Oath tiver um atributo reduzido durante uma batalha, aumente 2 pontos em sua Força.',
    'Duro de Ferir': 'A primeira vez que este Oath receberia dano durante uma batalha, reduza esse dano a zero. Armadilhas de Entrada, Condições Climáticas e Ailments de Status não ativam essa habilidade',
    'Download': 'Quando este Oath entra em batalha, ele escaneia o oponente. Em seguida, aumenta 1 ponto em Força, Destreza ou Poder Mágico, conforme o maior atributo do oponente.',
    'Drizzle': 'Quando este Oath entra em campo, ele automaticamente inicia os efeitos de Clima Chuvoso. Este efeito dura 4 rodadas.',
    'Drought': 'Quando este Oath entrar em campo, ele automaticamente inicia os efeitos do Clima Ensolarado. Este efeito dura 4 rodadas.',
    'Dry Skin': 'Se o Clima Ensolarado estiver em efeito, este Oath receberá 1 de dano no final de cada rodada. Ataques de Fogo causarão 1 de dano adicional a este Oath. Ataques de Água podem curar 1 HP deste Oath em vez de causar dano.',
    'Early Bird': 'O tempo que este Oath estaria adormecido é reduzido pela metade; ele precisará de apenas 2 sucessos para acordar na batalha.',
    'Effect Spore': 'Se for atingido por um Ataque Físico de Curto Alcance, o Oath rola 3 Dados de Chance para Envenenar, Paralisar ou Adormecer o inimigo aleatoriamente.',
    'Filter': 'Se um inimigo usar um movimento que causaria Dano Super efetivo a este Oath, reduza em 1 o Dano total causado por esse ataque.',
    'Flame Body': 'Quando atingido por um Ataque Físico de Curto Alcance, este Oath rola 3 Dados de Chance para Queimar o inimigo.',
    'Flame Boost': 'Se este Oath ficar com a condição de Queimado, aumente em 2 pontos seu atributo de Força ou Poder Mágico.',
    'Flash Fire': 'Na primeira vez que este Oath for atingido por um movimento do tipo Fogo, adicione 1 Dado Extra à Pool de Dano dos movimentos do tipo Fogo que este Oath usar até o final da cena. Movimentos do tipo Fogo não causam dano a este Oath.',
    'F-Gifter': 'Se o Clima Ensolarado estiver em efeito, aumente em 2 pontos o Atributo de Força e a Def. Mágica do usuário e de seus aliados.',
    'F-Veil': 'O usuário e seus aliados não podem ter seus Atributos reduzidos. O usuário e seus aliados não podem ter nenhuma Condição de Status infligida a eles. Reduções de Atributos e/ou enfermidades previamente infligidas permanecem.',
    'Fluffy': 'Reduza em 2 o Dano causado a este Oath por todos os Ataques Físicos. Aumente em 2 o Dano causado a este Oath por Ataques do tipo Fogo.',
    'Forecast': 'O Tipo primario deste Oath mudará dependendo do clima ativo: Fogo sob Sol, Água sob Chuva, Gelo sob Granizo e Pedra sob Areia.',
    'Forewarn': 'Durante a batalha, escolha um move de dano aleatoriamente do seu oponente, até o fim do combate você recebe 2 dados a menos de dano do move escolhido.',
    'Full Metal Body': 'Você recebe dois dados a menos de dano de ataques de Pedra, Metal, Terra, Grama, Agua, Gelo, Normal e Veneno. Você recebe 2 dados adicionais de dano de Fogo',
    'Fur Armor': 'Reduza em 2 o dano causado a este Oath por todos os Ataques Físicos.',
    'Gale Elements': 'Adicione "Prioridade" a todos os Movimentos do Tipo Primario deste Oath.',
    'Galvanize': 'Moves de ataque do Tipo Normal que este Oath usar são considerados do tipo Elétrico, afetando STAB, fraqueza e resistência. Adicione 1 Dado Extra de Dano aos Movimentos Elétricos.',
    'Aerilate': 'Os ataques do tipo Normal que o Oath usarão causarão dano como se fossem do tipo Voador, afetando STAB, fraqueza e resistência. Adicione 1 dado de dano aos movimentos do tipo Voador.',
    'Gluttony': 'Este Oath pode usar qualquer consumivel que estiver segurando em qualquer momento da batalha como uma ação livre.',
    'Gooey': 'A primeira vez que um oponente acertar este Oath com um Ataque Físico Não à Distância, reduza 1 ponto do seu Atributo de Destreza.',
    'War Tactics': 'No início da luta, escolha um movimento. Aumente em 1 ponto o Atributo de Força ou Poder Mágico deste Oath, ele só poderá executar o movimento escolhido, mas poderá Esquivar-se em todas as Rodadas. Este efeito é reiniciado se o Oath for retirado da batalha.',
    'Grass Armor':'A primeira vez que este receber dano de um ataque do tipo Grama, Agua, Pedra ou Terra, aumente em 2 pontos o Atributo de Defesa Física ou Mágica deste Oath.',
    'Grassy Surge':'Quando este Oath entra em campo, ele automaticamente inicia os efeitos do movimento Campo de Grama por 4 rodadas.',
    'Guts': 'Enquanto estiver afetado por uma Condição de Status, aumente em 2 pontos o Atributo de Força ou Poder Mágico deste Oath.',
    'Food Generator': 'Se este Oath usar um consumivel como item durante uma luta, o mesmo crescerá novamente após realizar um Switch (Trocar o Oath no combate). Funciona até 3 vezes por combate.',
    'Healer': 'Se um aliado no campo de batalha tiver uma Alergia de Status, no final da rodada, este Oath rola 3 Dados de Chance para curá-lo.',
    'Burn Proof': 'Burn Status não causa dano a este Oath nem reduz sua Força. Se este Oath for atingido por um Ataque do Tipo Fogo, reduza o dano causado em 2.',
    'Heavy Belly': 'Movimentos com dano baseado no peso recebem +2 dados de dano.',
    'Honey Gather': 'Se não estiver segurando consumivel no inicio da rodada, cria um Honey (Chance de curar um Status em 3d6 ou recupera 1 PV). Funciona até 3 vezes no combate. Ao fim do combate se estiver com um honey equipado ele é consumido automaticamente.',
    'Huge Power': 'Este Oath tem um aumento permanente  de 1 ponto em seu atributo de Força.',
    'Hustle': 'Este Oath recebe uma redução adicional de Acuracia e 2 Dados Extras nas jogadas de dano para todos os seus Ataques Físicos ou Mágicos.',
    'Rain Lover': 'Quando o clima de Chuva estiver em efeito, este Oath curará qualquer condição de status que tiver no final da rodada.',
    'Hyper Cutter': 'Este Oath não pode ter seu Atributo de Força reduzido por nenhum meio. Sempre que aumentar sua Força, aumente em +1.',
    'Ice Body': 'Se o clima de Granizo estiver em efeito, você pode restaurar 1 PV a este Oath no final da rodada. Este Oath é imune a danos do clima de Granizo.',
    'Ice Scales': 'Reduza em 2 o dano causado a este Oath por todos os Ataques Mágicos',
    'Immunity': 'As condições de Status de Veneno e Veneno Grave não causam dano a este Oath.',
    'Imposter': 'Ignora qualquer efeito que aumente a defesa do alvo, ou ignore o dano.',
    'Inner Focus': 'Este Oath não sofre Flinch e ignora a primeira vez que algum Oath for reduzir um Status dele (Ele ainda pode reduzir seu proprio status sem ativar está habilidade.)',
    'Insomnia': 'Este Oath é imune ao status Sono.',
    'Intimidate': 'Quando este Oath entra em batalha, reduza 1 ponto na Força de todos os inimigos na área',
    'Iron Barbs': 'Sempre que este Oath for atingido por um Ataque Físico Não à Distância, causa 1 de dano contra o atacante',
    'Iron Fist': 'Adicione 1 Dado à pool de dano de movimentos baseados em socos.',
    'Justified': 'A primeira vez que este Oath for atingido por um Ataque do Tipo Sombrio, Fantasma ou Psiquico, aumente em 1 ponto seu Atributo de Força.',
    'Keen Eye': 'Este Oath não pode ter sucessos removidos de seus rolamentos de Precisão por Movimentos, Itens ou Habilidades.',
    'Klutz': 'Seus consumiveis seguraveis e os do oponente perdem efeito enquanto este Oath está em batalha.',
    'Assassin': 'Acertos criticos tem chance de 3 dados de causar Burn, Poison ou Paralisia aleatoriamente.',
    'Levitate': 'Movimentos do tipo Terra e efeitos no chão não afetarão este Oath. Se um Oath usar um movimento que o prende ao chão, os efeitos serão perdidos até que ele esteja livre novamente.',
    'Libero': 'Sempre que este Oath usar um movimento, primeiro mude seu tipo para o do movimento. Se o movimento for um ataque e causar dano, use o STAB apropriado.',
    'Adaptability': 'Sempre que este Oath usar um Movimento Danoso que corresponda ao seu Tipo, adicione 1 Dados de Bônus nas jogadas de dano.',
    'Aerilate': 'Ataques do Tipo Normal que o Oath usar causarão dano como se fossem do Tipo Voador, afetando STAB, fraqueza e resistência. Adicione 1 Dado de dano aos movimentos do tipo Voador.',
    'Lightning Rod': 'Se alguém usar um movimento do Tipo Elétrico com um único alvo, ele será redirecionado para este Oath; ele é imune a dano de tais movimentos. A primeira vez que este Oath for atingido por um movimento do Tipo Elétrico, aumente 2 Pontos no Poder Mágico deste Oath.',
    'Limber': 'Este Oath não é afetado pelo Status de Paralisia.',
    'Liquid Ooze': 'Se for atingido por um movimento que absorveria os pontos de vida deste Oath (Semente Suculenta, Efeito Sonho, Soco de Drenagem, etc.), ele causará em vez disso essa quantidade como dano.',
    'Long Reach': 'Todos os ataques feitos por este Oath são considerados ataques à distância.',
    'Magic Bounce': 'Todos os movimentos que não são de dano que visam este Oath ou seu lado do campo de batalha terão seus efeitos redirecionados para os adversários.',
    'Magic Guard': 'Este Oath não receberá dano de Condições de Status, Recuo, Itens Segurados ou Condições Climáticas.',
    'Magician': 'Este Oath irá roubar o Item Segurado de um adversário que ele acabou de atingir com um ataque fisico não a distancia.',
    '': '',
    '': '',
    '': '',
    '': '',
    '': '',
    '': '',
    '': '',
    '': '',
    '': '',
    '': '',
    '': '',
    '': '',
    '': '',
    '': '',
    '': '',
    '': '',
    '': '',
    '': '',
    '': '',
    '': '',
    '': '',
    '': '',
    '': '',
    '': '',
}

# Vantagens Lendárias:
vantagens_lendarias = {
    'Intrepid Sword':'Sempre que este Oath entra em batalha, aumente em 2 pontos sua Força.',
}

# Estilos de combate de cada Oath:
estilos = {
    # Aumentam dano para Ataques Físicos:
    "⚔️ Guerreiro": "+1 dano para ataques físicos, -1 dano para ataques mágicos.",
    "💥 Berserker": "+1 dano para ataques físicos, -1 na defesa mágica.",
    "🛡️ Agressor": "+1 dano para ataques físicos, -1 na defesa física.",
    "⚡ Impacto": "+1 dano para ataques físicos, -1 na esquiva.",
    # Aumentam dano para Ataques Mágicos:
    "🧙 Mago": "+1 dano para ataques mágicos, -1 dano para ataques físicos.",
    "🔮 Arcanista": "+1 dano para ataques mágicos, -1 na defesa física.",
    "🌌 Místico": "+1 dano para ataques mágicos, -1 na defesa mágica.",
    "🌀 Ilusionista": "+1 dano para ataques mágicos, -1 na esquiva.",
    # Aumentam a Defesa Física:
    "🔰 Guardião": "+1 na defesa física, -1 no dano para ataques mágicos.",
    "🛡️ Defensor": "+1 na defesa física, -1 no dano para ataques físicos",
    "🦸‍♂️ Fortificador": "+1 na defesa física, -1 na esquiva.",
    "🏰 Bastião": "+1 na defesa física, -1 na defesa mágica.",
    # Aumentam a Defesa Mágica:
    "🦸‍♂️ Protetor": "+1 na defesa mágica, -1 dano para ataques físicos.",
    "🔮 Desfocado": "+1 na defesa mágica, -1 no dano para ataques mágicos.",
    "✨ Barreira": "+1 na defesa mágica, -1 na esquiva.",
    "🌈 Aegis": "+1 na defesa mágica, -1 na defesa física.",
    # Aumentam Acurácia:
    "⚖️ Equilibrado": "+1 na Acurácia, -1 no dano para ataques físicos.",
    "🚀 Acelerador": "+1 na Acurácia, -1 no dano para ataques mágicos.",
    "🔭 Focalizador": "+1 na Acurácia, -1 na defesa física.",
    "🏹 Precisão": "+1 na Acurácia, -1 na defesa mágica.",
    # Aumentam Esquiva:
    "🌑 Sombra": "+1 na esquiva, -1 na defesa física.",
    "⚡ Evasor": "+1 na esquiva, -1 na defesa mágica.",
    "⚡ Velocista": "+1 na esquiva, -1 no dano para ataques físicos",
    "⚡ Escapista": "+1 na esquiva, -1 no dano para ataques mágicos.",
    # Aumentam Vida:
    "❤️ Guardião": "+1 de vida, -1 na defesa mágica.",
    "🔋 Sustentador": "+1 de vida, -1 no dano para ataques físicos.",
    "🌌 Resiliênte":"+1 de vida, -1 no dano para ataques mágicos.",
    "🌿 Vitalidade": "+1 de vida, -1 na defesa física.",
    # Aumentam Mana:
    "📜 Mestre de Mana": "+1 de Mana, -1 no dano para ataques físicos.",
    "🌌 Amplificador": "+1 de Mana, -1 no dano para ataques mágicos.",
    "🧩 Tático": "+1 de Mana, -1 na defesa mágica.",
    "🔋 Energizador": "+1 de Mana, -1 na defesa física.",
    # Neutros:
    "🌀 Sereno": "Neutro (Não aumentam nem reduzem nenhuma rolagem).",
    "🧩 Equilibrado": "Neutro (Não aumentam nem reduzem nenhuma rolagem).",
    "✨ Universal": "Neutro (Não aumentam nem reduzem nenhuma rolagem).",
    "🌟 Preguiçoso": "Neutro (Não aumentam nem reduzem nenhuma rolagem).",
}

# Tipagem:
tipos = [
    'Normal',
    '🔥 Fogo',
    '💧 Água',
    '🌿 Grama',
    '🕊️ Voador',
    '👊 Lutador',
    '☠️ Veneno',
    '⚡ Elétrico',
    'Terra',
    'Pedra',
    '🔮 Psíquico',
    '❄️ Gelo',
    '🐞 Inseto',
    '👻 Fantasma',
    '⚙️ Metal',
    '🐉 Dragão',
    '🌑 Sombrio',
    '🧚 Fada'
]

# Efeitos para Moves:
moveseffect = {}

efnega = [
    'Redução de Acurácia 1',
    'Redução de Acurácia 2',
    'Recuo',
    'Reduza sua Força em 1',
    'Reduza sua Destreza em 1',
    'Reduza sua Def. Fisica em 1',
    'Reduza sua Def. Mágica em 1'
]

efposi = {}

# Parte da ficha Base dos jogadores:
ficha_jogadorMX = {
    'Força': 5,
    'Destreza': 5, 
    'Inteligencia': 5, 
    'Durabilidade': 5, 
    'Foco': 5
}
ficha_jogadorAT = {
    'Força': 1,
    'Destreza': 1, 
    'Inteligencia': 1, 
    'Durabilidade': 1, 
    'Foco': 1
}
status_jogadorMX = {
    # Combate:
    'Ataque': 5,
    'Precisão': 5,
    'Esquiva': 5,
    # Sobrevivência:
    '': 5,
    '': 5,
    '': 5,
    '': 5,
    # Social:
    '': 5,
    '': 5,
    '': 5,
    '': 5,
    # Extras:
    '': 5,
    '': 5,
    '': 5,
    '': 5,

    
}

# Ficha do jogador:
def exibir_ficha_jogador (ficha_jogadorMX, ficha_jogadorAT):
    print("Nome:\nIdade:")
    for nm in ficha_jogadorMX:
        distribuido = '•' * ficha_jogadorAT[nm]
        distribuir = 'o' * (ficha_jogadorMX[nm] - ficha_jogadorAT[nm])
        print(f"🔹 {nm}: {distribuido}{distribuir}")