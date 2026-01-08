import sys
import mariadb
from config import USER, PASSWORD, HOST, PORT, DATABASE

class DatabaseManager:
    def __init__(self):
        self.user = USER
        self.password = PASSWORD
        self.host = HOST
        self.port = PORT
        self.database = DATABASE

    async def connect(self):
        try:
            conn = mariadb.connect(
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port,
                database=self.database
            )
            return conn
        except mariadb.Error as e:
            print(f"Ошибка подключения: {e}")
            sys.exit(1)

    async def add_birthday(self, ds_id: int, date_birthday):
        conn = await self.connect()
        cur = conn.cursor()

        try:
            cur.execute("SELECT ds_id FROM happy_birthday WHERE ds_id = ?", (ds_id,))
            if cur.fetchone():
                return "Запись в БД уже существует. Используй $update_birthday для изменения."
            

            cur.execute("INSERT INTO happy_birthday (ds_id, date_birthday) VALUES (?, ?)", (ds_id, date_birthday))
            conn.commit()

            return None

        except mariadb.Error as e:
            print(f"Ошибка выполнения запроса: {e}")
            return []
        finally:
            conn.close()

    async def remove_birthday(self, ds_id: int):
        conn = await self.connect()
        cur = conn.cursor()

        try:
            cur.execute("DELETE FROM happy_birthday WHERE ds_id = ?", (ds_id,))
            conn.commit()
            return cur.rowcount
        except mariadb.Error as e:
            print(f"Ошибка выполнения запроса: {e}")
            return 0
        finally:
            conn.close()

    async def update_birthday(self, ds_id: int, date_birthday):
        conn = await self.connect()
        cur = conn.cursor()

        try:
            cur.execute("UPDATE happy_birthday SET date_birthday = ? WHERE ds_id = ?", (date_birthday, ds_id))
            conn.commit()
            return cur.rowcount
        except mariadb.Error as e:
            print(f"Ошибка выполнения запроса: {e}")
            return 0
        finally:
            conn.close()

    async def get_info_birthday(self):
        conn = await self.connect()
        cur = conn.cursor()

        try:
            cur.execute("SELECT ds_id, date_birthday FROM happy_birthday")
            rows = cur.fetchall()
            return rows
        except mariadb.Error as e:
            print(f"Ошибка выполнения запроса: {e}")
            return []
        finally:
            conn.close()