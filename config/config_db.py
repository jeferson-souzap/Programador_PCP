import sqlite3

conn = sqlite3.connect(r"D:\#Mega\Jeferson - Dev\02 - Linguagens\Python\Programador_PCP\db\programador.db")
cursor = conn.cursor()

# Tabela de usuários
cursor.execute("""
CREATE TABLE IF NOT EXISTS usuario (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL
)
""")

conn.commit()
conn.close()
