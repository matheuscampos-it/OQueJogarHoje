import requests
import pandas as pd
import time

API_KEY = "5b42a28ceb234a5da8d6d1105ae75894"
BASE_URL = "https://api.rawg.io/api/games"

# Slugs corretos dos gêneros segundo a RAWG API
GENEROS = {
    "action": "Action",
    "indie": "Indie",
    "adventure": "Adventure",
    "role-playing-games-rpg": "RPG",
    "strategy": "Strategy",
    "simulation": "Simulation",
    "shooter": "Shooter",
    "sports": "Sports"
}

headers = {"User-Agent": "MagoDosDados/1.0"}
jogos_coletados = []

for slug, nome_genero in GENEROS.items():
    print(f"🔍 Coletando jogos do gênero: {nome_genero}")
    for page in range(1, 4):  # Até 3 páginas por gênero (máx. 300 jogos)
        params = {
            "genres": slug,
            "page": page,
            "page_size": 100,
            "key": API_KEY
        }

        response = requests.get(BASE_URL, headers=headers, params=params)

        if response.status_code == 200:
            data = response.json()
            for jogo in data['results']:
                jogos_coletados.append({
                    "nome": jogo.get("name"),
                    "genero": nome_genero,
                    "rating": jogo.get("rating"),
                    "playtime": jogo.get("playtime"),
                    "lancamento": jogo.get("released")
                })
        else:
            print(f"⚠️ Erro na requisição ({nome_genero}, página {page}): {response.status_code}")
        time.sleep(1.2)  # Previne rate limit

# Criar DataFrame e salvar em CSV
df = pd.DataFrame(jogos_coletados)
df.to_csv("jogos_rawg.csv", index=False, encoding="utf-8")
print(f"\n✅ Coleta finalizada. Total de jogos coletados: {len(df)}")
print("📁 Arquivo salvo como 'jogos_rawg.csv'")
