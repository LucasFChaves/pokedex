import sqlite3
import json

# Seu JSON de pokémons
with open('pokemons.json', 'r', encoding='utf-8') as f:
    pokemons = json.load(f)


# Conectar ao banco
conn = sqlite3.connect('app/pokemons.db')
cursor = conn.cursor()

# Função para garantir que um tipo exista e retornar seu código
def obter_ou_criar_tipo(nome_tipo):
    cursor.execute("SELECT codigo FROM tipo WHERE nome = ?", (nome_tipo,))
    resultado = cursor.fetchone()
    if resultado:
        return resultado[0]
    cursor.execute("INSERT INTO tipo (nome) VALUES (?)", (nome_tipo,))
    conn.commit()
    return cursor.lastrowid

# Inserir pokémons
for p in pokemons:
    tipo1_id = obter_ou_criar_tipo(p["tipo_primario"])
    tipo2_id = obter_ou_criar_tipo(p["tipo_secundario"]) if p["tipo_secundario"] else None

    cursor.execute("""
        INSERT OR REPLACE INTO pokemon (codigo, nome, codigo_tipo_primario, codigo_tipo_secundario)
        VALUES (?, ?, ?, ?)
    """, (p["codigo"], p["nome"], tipo1_id, tipo2_id))

conn.commit()
conn.close()

print("Pokémons inseridos com sucesso.")

