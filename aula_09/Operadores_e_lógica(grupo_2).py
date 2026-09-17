import pandas as pd
import io

# =========================================================
# 1. EXEMPLOS ARITMÉTICOS (Slides 8 e 9)
# =========================================================
# ADIÇÃO
dano_espada = 15
dano_magico = 10
total_de_dano = dano_espada + dano_magico
print(total_de_dano)  # Saída: 25

# SUBTRAÇÃO (20 - 33 resulta em -13)
vida_atual = 20
vida_maxima = 33
vida_perdida = vida_atual - vida_maxima
print(vida_perdida)  # Saída: -13

# MULTIPLICAÇÃO
dano_critico = total_de_dano * 2
print(dano_critico)  # Saída: 50

# DIVISÃO
valor_totalXP = 1000
membros_grupo = 5
xp_por_membro = valor_totalXP / membros_grupo
print(xp_por_membro)  # Saída: 200.0

print("\n" + "="*40 + "\n")

# =========================================================
# 2. EXEMPLOS DE COMPARAÇÃO (Slide 10)
# =========================================================
teste_personagem = 10
dificuldade_exigida = 12

print(teste_personagem >= dificuldade_exigida)  # Saída: False

classe_personagem = "Guerreiro"
print(classe_personagem == "Feiticeiro")         # Saída: False
print(classe_personagem != "Mago")               # Saída: True

print("\n" + "="*40 + "\n")

# =========================================================
# 3. EXEMPLOS DE OPERADORES LÓGICOS (Slide 11)
# =========================================================
tem_chave = True
porta_destrancada = False

esta_invisivel = False
if not esta_invisivel:
    print("Os inimigos podem te ver!")

if tem_chave and not porta_destrancada:
    print("Você destranca a porta com a chave.")

carisma_alto = False
forca_alta = True

if carisma_alto or forca_alta:
    print("Você conseguiu convencer ou intimidar o goblin.")

print("\n" + "="*40 + "\n")

# =========================================================
# 4. EXEMPLOS DE ERROS COMUNS (Slides 14 e 15)
# =========================================================
# 1. Atribuição vs Comparação
vida = 100
esta_vivo = vida == 100

# 2. Divisão Decimal vs Inteira
dano_float = 15 / 2
dano_int = 15 // 2

# 3. Precedência e Parênteses
dano_errado = 10 + 5 * 2
dano_certo = (10 + 5) * 2

print(f"Está vivo?: {esta_vivo}")
print(f"Dano inteiro: {dano_int}")
print(f"Dano errado (sem parênteses): {dano_errado}")
print(f"Dano certo (com parênteses): {dano_certo}")

print("\n" + "="*40 + "\n")

# =========================================================
# 5. APLICAÇÃO EM DADOS (Slides 16 e 17)
# =========================================================
csv_data = """id_jogador,classe,nivel,tempo_jogo
1,Mago,12,120
2,Guerreiro,8,45
3,Mago,5,20
4,Ladino,12,-15
5,Clerigo,10,90
6,Mago,12,200
7,Bardo,4,-5"""

df_jogadores = pd.read_csv(io.StringIO(csv_data))

# 1. Filtrando uma segmentação específica de Jogadores
magos_nv12 = df_jogadores.query("classe == 'Mago' and nivel == 12")
print("Magos Nível 12:")
print(magos_nv12)

print("\n-------------------------\n")

# 2. Limpeza de Dados (Barrer valores impossíveis)
dados_limpos = df_jogadores.query("not tempo_jogo < 0")
print("Dados Limpos:")
print(dados_limpos)