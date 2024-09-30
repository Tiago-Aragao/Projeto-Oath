# Gera Nomes Aleatórios baseados em Prefixo, Sufixo e Silabas:

# Importações:
import random
#from Gerar_Oath import sexo

def Gerar_Nomes_Random():
    
    # Listas de prefixos, sufixos, titulos e sílabas:
    titulosmasc = [
    "Dr.", "Sr.", "Eng.", "Prof.", "Adv.", "Arq.", "M.", "Ps.", 
    "T.", "Capt.", "Gen.", "P.", "Mec.", "Enf.", "C."
    ]
    titulosfemi = [
    "Dra.", "Sra.", "Enga.", "Profa.", "Adva.", "Arqa.", "M.", 
    "Psa.", "T.", "Capa.", "Gen.", "Enfa.", "Mec.", "D.", "C."
    ]
    prefixos = [
    "Ael", "Al", "Alti", "Ara", "Arb", "Ari", "Astra", "Ayla", 
    "Bai", "Bar", "Bari", "Bel", "Boko", "Brin", "Cai", "Cal", "Caro", 
    "Calae", "Cer", "Chai", "Ciri", "Dai", "Dar", "Darae", "Drax", 
    "Dur", "Elys", "Ember", "Erae", "Eri", "Fai", "Farae", "Fen", "Fira", 
    "Fino", "Gai", "Garae", "Gal", "Gali", "Gry", "Hal", "Hala", "Hari", 
    "Hel", "Hyn", "Iarae", "Isar", "Jai", "Jan", "Jas", "Jora", "Jarae", 
    "Ka", "Kael", "Kall", "Kai", "Kano", "Kari", "Kiro", "Kyra", "La", 
    "Lano", "Larae", "Lari", "Lumos", "Mai", "Mar", "Marae", "Myn", 
    "Nai", "Nera", "Neko", "Nyl", "Noi", "Odin", "Oris", "Ora", "Orin", 
    "Pari", "Piko", "Qari", "Qira", "Quin", "Ra", "Rael", "Rari", 
    "Riven", "Rhea", "Sai", "Sarae", "Sari", "Sel", "Sera", "Sora", 
    "Tari", "Talon", "Tel", "Thal", "Tho","Ti" ,"Tira", "Timo", "Uma", 
    "Uari", "Ula", "Val", "Vari", "Vex", "Vira", "Vyn", "Wai", "Wren", 
    "Wiro", "Xai", "Xal", "Xen", "Xylo", "Yara", "Yly", "Zai", 
    "Zeni", "Zor", "Zyn", "Zari", "Po", "Des","Mata", "Ku"
    ]
    silabas = [
    "a", "ai", "al", "an", "ar", "as", "at", "au", "ba", "be", 
    "bi", "bu", "bu", "ca", "cha", "ce", "ci", "co", "cu", "da", 
    "de", "di", "do", "du", "e", "ei", "el", "em", "en", "es", 
    "et", "fa", "fai", "fi", "fo", "ga", "ga", "ge", "gi", "go", 
    "ha", "hai", "he", "hi", "ho", "hu", "ja", "je", "ji", "jo", 
    "ju", "ka", "kai", "ke", "ki", "ko", "ku", "la", "lai", "le", 
    "li", "lo", "lu", "ma", "mai", "me", "mi", "mo", "mu", "na", 
    "nai", "ne", "ni", "no", "nu", "o", "pa", "pai", "pe", "pi", 
    "po", "ra", "rei", "ri", "ro", "ru", "sa", "sei", "shi", "si", 
    "ta", "tai", "te", "ti", "tu", "va", "ve", "vi", "wu", "ya", 
    "ye", "yi", "za", "zai", "ze", "zi", "zo", "xu", "xi", "ra"
    "xe", "wo", "wu", "yu", "yo", "zu", "rru", "gra", "gay"
    ]
    sufixos = [
    "ael", "aen", "ach", "air", "al", "alith", "an", "anith", "ar", "aris", "as",
    "ash", "dão", "dan", "dor", "du", "el", "elios", "elith", "elth", "en", "enith",
    "enor", "eth", "ethar", "ex", "gão", "ia", "iah", "ian", "iax", "ich", "ik",
    "ilith", "in", "inor", "inys", "ion", "ionel", "ionis", "ir", "ith", "ithor",
    "ithra", "ka", "kan", "lin", "linos", "lyon", "myr", "ol", "on", "or", "osis",
    "osia", "oth", "pika", "rel", "ris", "rion", "ran", "s", "th", "thinha", "tal",
    "ul", "un", "unel", "ur", "ver", "wyn", "yth", "yra", "ythe", "yn", "ynar"
    ]

    # Escolhendo aleatoriamente um prefixo, uma sílaba e um sufixo:
    
    # Adicionando um titulo: FUTURAMENTE
    '''
    if sexo == "Masc":
        if random.random() < 0.05:
            nome = random.choice(titulosmasc)
    else:
        if random.random() < 0.05:
            nome = random.choice(titulosfemi)
    '''
    
    # Adicionando um prefixo:
    nome = random.choice(prefixos)

    # Adicionando apenas uma silaba com 50% de chance de ter ou não:
    if random.random() < 0.30:
        nome += random.choice(silabas)
    
    # Adicionando um sufixo com 30% de chance de ter ou não:
    if random.random() < 0.70:
        nome += random.choice(sufixos)
    
    return nome