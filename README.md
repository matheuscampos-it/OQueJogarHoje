# O Que Jogar Hoje?

````markdown
# 🎮 O Que Jogar Hoje? – Recomendador de Jogos com RAWG API + Python + Power BI

Bem-vindo(a) ao projeto **“O Que Jogar Hoje?”**, um sistema de recomendação de jogos baseado nas
preferências do usuário (gênero, tempo disponível e avaliação da crítica),
utilizando a **RAWG API**, **Python** para tratamento de dados
e um **dashboard interativo em Power BI**.

> ⚡ Ideal para quem tem pouco tempo e muitas opções na biblioteca!

---

## 📌 Visão Geral

Você já abriu sua lista de jogos e ficou paralisado sem saber o que jogar?  
Esse projeto resolve isso para você com sugestões inteligentes baseadas no **seu tempo livre**,
 **gêneros favoritos** e **jogos bem avaliados pela comunidade**.

---

## 🧰 Tecnologias Utilizadas

| Ferramenta | Função |
|------------|--------|
| 🔗 [RAWG API](https://rawg.io/apidocs) | Coleta de dados sobre jogos (gênero, avaliação, tempo de jogo) |
| 🐍 Python + Pandas | Tratamento, filtragem e enriquecimento dos dados |
| 📊 Power BI | Dashboard interativo com filtros e recomendação aleatória |
| 📝 Notion | Documentação do projeto e devlog |

````

---

## 🚀 Etapas do Projeto

1. **Definição dos critérios de recomendação**
   🎯 Gênero (8 opções) + Tempo disponível (Curto, Médio, Longo) + Nota mínima (rating)

2. **Coleta de dados com RAWG API**
   🔍 +500 jogos buscados com Python + `requests`

3. **Tratamento e enriquecimento com Pandas**
   🧹 Exclusão de jogos sem nota ou tempo, categorização por tempo, criação de coluna `recomendado`

4. **Criação do Dashboard no Power BI**
   🧠 Filtros interativos + recomendação aleatória + top 5 jogos por avaliação

5. **Documentação e publicação**
   📘 Devlogs no Notion + versão pública do dashboard no Power BI Service (em breve)

---

## 🖥️ Prints do Dashboard



---

## 📌 Exemplos de Filtros

| Gênero | Tempo Disponível | Nota mínima | Resultado Sugerido       |
| ------ | ---------------- | ----------- | ------------------------ |
| RPG    | Longo (+20h)     | 4 estrelas  | The Witcher 3: Wild Hunt |
| Action | Curto (-10h)     | 3 estrelas  | Katana ZERO              |

---

## ✨ Funcionalidades Extras Futuras

* Exportar a recomendação para PDF
* Adicionar imagens e links dos jogos no dashboard
* Interface Web em Flask ou Streamlit (versão futura)
* Gravar um vídeo com a explicação do projeto para o YouTube

---

## 👨‍💻 Autor

Desenvolvido por *Matheus Campos*, entusiasta de dados, jogos e boas visualizações.
🔗 [LinkedIn](https://www.linkedin.com/in/matheus-campos-it/) | 📧 [campos98matheus@gmail.com](mailto:campos98matheus@gmail.com)

---

## 📜 Licença

Este projeto é open-source e você pode adaptá-lo como quiser!

---

🎮 *Hora de jogar!*
