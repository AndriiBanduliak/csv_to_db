
import pandas as pd
import sqlite3

# Чтение данных из CSV файла
data = pd.read_csv('you csv file.csv')

# Установка соединения с базой данных SQLite
conn = sqlite3.connect('db_1.db')

# Запись данных в базу данных
data.to_sql('table_name', conn, if_exists='replace')
