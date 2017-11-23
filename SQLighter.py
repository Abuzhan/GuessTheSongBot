import sqlite3

class SQLighter:

    def __init__(self, database):
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    def check_new_user(self, chat_id):
        with self.connection:
            if self.cursor.execute('SELECT * FROM users WHERE chat_id = ?', (chat_id,)).fetchone():
                return True
            else:
                return False

    def save_user(self, chat_id):
        with self.connection:
            self.cursor.execute('INSERT INTO users (chat_id) VALUES (?)', (chat_id,))
            return True

    def reset_user(self, chat_id):
        with self.connection:
            self.cursor.execute('UPDATE users SET score = 0, song_id = 1 WHERE chat_id = ?', (chat_id,))

    def get_user(self, chat_id):
        with self.connection:
            return self.cursor.execute('SELECT * FROM users WHERE chat_id =?', (chat_id,)).fetchone()

    def add_score(self,chat_id):
        with self.connection:
            self.cursor.execute('UPDATE users SET score = score + 1, song_id = song_id + 1 WHERE chat_id = ?', (chat_id,))

    def add_song_id(self,chat_id):
        with self.connection:
            self.cursor.execute('UPDATE users SET song_id = song_id + 1 WHERE chat_id = ?', (chat_id,))

    def select_all(self):
        """ Получаем все строки """
        with self.connection:
            return self.cursor.execute('SELECT * FROM music').fetchall()

    def select_single(self, rownum):
        """ Получаем одну строку с номером rownum """
        with self.connection:
            return self.cursor.execute('SELECT * FROM music WHERE id = ?', (rownum,)).fetchall()[0]

    def count_rows(self):
        """ Считаем количество строк """
        with self.connection:
            result = self.cursor.execute('SELECT * FROM music').fetchall()
            return len(result)

    def close(self):
        """ Закрываем текущее соединение с БД """
        self.connection.close()
