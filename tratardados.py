import pandas as pd

# Carregar o CSV bruto exportado da API RAWG
df = pd.read_csv("jogos_rawg.csv")

# 🔹 1. Remover jogos sem nota ou sem tempo de jogo
df = df.dropna(subset=["rating", "playtime"])
df = df[df["playtime"] > 0]

# 🔹 2. Classificar tempo de jogo em categorias
def classificar_tempo(playtime):
    if playtime < 10:
        return "Curto"
    elif 10 <= playtime <= 20:
        return "Médio"
    else:
        return "Longo"

df["tempo_categoria"] = df["playtime"].apply(classificar_tempo)

# 🔹 3. Criar coluna 'recomendado' com base em critérios mínimos
# Aqui, como exemplo, definimos recomendado como rating > 3.5
df["recomendado"] = df["rating"] >= 3.5

# 🔹 4. Exportar para novo CSV tratado
df.to_csv("jogos_tratados.csv", index=False)

print("✅ Dados tratados e exportados para jogos_tratados.csv!")
