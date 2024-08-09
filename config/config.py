import mysql.connector

# Configuração da conexão
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="audios"
)

cursor = connection.cursor()

# Ler e executar o script SQL
with open('audio/database/db.sql', 'r') as file:
    sql_script = file.read()

# Executar o script SQL
try:
    cursor.execute(sql_script, multi=True)
    connection.commit()
    print("Rodou com sucesso!")
except mysql.connector.Error as err:
    print(f"Erro: {err}")

connection.close()
