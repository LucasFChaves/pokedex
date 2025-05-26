import sqlite3
import os

DB_NAME = 'pokemons.db'

print("Usando banco em:", os.path.abspath(DB_NAME))

def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row  # Retorna dicionários
    return conn