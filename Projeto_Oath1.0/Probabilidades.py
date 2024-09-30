# Define quais atributos e suas probabilidades por TIER:
valores = {
    1: [3,4,5],
    2: [3,4,5,6],
    3: [3,4,5,6,7],
    4: [3,4,5,6,7,8],
    5: [3,4,5,6,7,8,9],
}
peso = {
    1: [0.30, 0.60, 0.10],
    2: [0.15, 0.45, 0.35, 0.05],
    3: [0.05, 0.35, 0.35, 0.15, 0.10],
    4: [0.10, 0.25, 0.30, 0.20, 0.10, 0.05],
    5: [0.05, 0.20, 0.30, 0.25, 0.20, 0.10, 0.05],
}

# Define quais atributos e suas probabilidades por TIER, mas para Lendários:
valoreslend = {
    1: [3,4,5,6,7],
    2: [4,5,6,7,8],
    3: [4,5,6,7,8,9],
}
pesolend = {
    1: [0.1, 0.2, 0.3, 0.3, 0.1],
    2: [0.1, 0.2, 0.35, 0.25, 0.1],
    3: [0.1, 0.2, 0.2, 0.2, 0.2, 0.1]
}

# Define probabilidades de ter moves de power de 1 a 6
valoresmoves = [
    1,
    2,
    3,
    4,
    5,
    6
]
pesomoves = [
    0.15,
    0.2,
    0.2,
    0.15,
    0.1,
    0.1
]

# Define probabilidade de ter ou não uma evolução:
valoresevo = {
    1: [1,2], # Tier 1: Branco
    2: [0,1,2], # Tier 2: Verde
    3: [0,1,2], # Tier 3: Azul
    4: [0,1], # Tier 4: Roxo
    5: [0], # Tier 5: Preto
}
pesoevo = {
    1: [0.50,0.50], # Tier 1: 80% de ter 1 Evolução, 20% de ter 2.
    2: [0.15,0.70,0.15], # Tier 2: 15% de não ter nenhuma Evolução, 70% de ter 1 e 15% de ter 2.
    3: [0.70,0.25,0.05], # Tier 3: 70% de não ter nenhuma Evolução, 25% de ter 1 e 5% de ter 2.
    4: [0.80,0.20], # Tier 4: 80% de não ter Evolução, 20% de ter 1.
    5: [0], # Tier 5: Não tem Evolução.
}

# Define o limite máximo para o maxatri, tornando os Oath's em teoria mais balanceados:
limite_maxatri = {
    1: 20,
    2: 20,
    3: 25,
    4: 25,
    5: 30,
}

limite_minatri = {
    1: 15,
    2: 15,
    3: 20,
    4: 20,
    5: 25,
}