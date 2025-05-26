import sqlite3
from .database import get_connection

def criar_tabelas():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tipo (
            codigo INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL UNIQUE
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pokemon (
            codigo INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            codigo_tipo_primario INTEGER NOT NULL,
            codigo_tipo_secundario INTEGER,
            FOREIGN KEY (codigo_tipo_primario) REFERENCES tipo(codigo),
            FOREIGN KEY (codigo_tipo_secundario) REFERENCES tipo(codigo)
        )
    ''')

    conn.commit()
    conn.close()

def inserir_tipo(nome):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO tipo (nome) VALUES (?)", (nome,))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def listar_tipos():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tipo")
    tipos = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return tipos

def obter_ou_criar_tipo(nome_tipo):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT codigo FROM tipo WHERE nome = ?", (nome_tipo,))
    row = cursor.fetchone()
    if row:
        conn.close()
        return row['codigo']
    cursor.execute("INSERT INTO tipo (nome) VALUES (?)", (nome_tipo,))
    conn.commit()
    tipo_id = cursor.lastrowid
    conn.close()
    return tipo_id

def inserir_pokemon(data):
    nome = data.get("nome")
    tipo_primario = data.get("tipo_primario")
    tipo_secundario = data.get("tipo_secundario")

    if not nome or not tipo_primario:
        return False

    tipo1_id = obter_ou_criar_tipo(tipo_primario)
    tipo2_id = obter_ou_criar_tipo(tipo_secundario) if tipo_secundario else None

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO pokemon (nome, codigo_tipo_primario, codigo_tipo_secundario)
        VALUES (?, ?, ?)
    """, (nome, tipo1_id, tipo2_id))
    conn.commit()
    conn.close()
    return True

def listar_pokemons():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT p.codigo, p.nome,
               t1.nome AS tipo_primario,
               t2.nome AS tipo_secundario
        FROM pokemon p
        JOIN tipo t1 ON p.codigo_tipo_primario = t1.codigo
        LEFT JOIN tipo t2 ON p.codigo_tipo_secundario = t2.codigo
    ''')
    pokemons = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return pokemons

if __name__ == '__main__':
    criar_tabelas()