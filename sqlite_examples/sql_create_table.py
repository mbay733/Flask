import sqlite3

create_table = """
CREATE TABLE IF NOT EXISTS quotes (
id INTEGER PRIMARY KEY AUTOINCREMENT,
author TEXT NOT NULL,
text TEXT NOT NULL
);
"""
# ПодключениевБД
connection = sqlite3.connect("store.db")

# Создаем cursor, он позволяет делать SQL-запросы
cursor = connection.cursor()

# Выполняемзапрос:
cursor.execute(create_table)

# Фиксируемвыполнение(транзакцию)
connection.commit()

# Закрытькурсор:
cursor.close()

# Закрытьсоединение:
connection.close()
