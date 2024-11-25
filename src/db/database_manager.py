import sqlite3


class DatabaseManager:
    def __init__(self, db_name="game_results.db"):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS game_results (
                id INTEGER PRIMARY KEY,
                player_name TEXT,
                attempts INTEGER,
                correct_guesses INTEGER,
                time_spent REAL
            )
        """
        )
        self.conn.commit()

    def save_game_result(self, player_name, attempts, correct_guesses, time_spent):
        self.cursor.execute(
            """
            INSERT INTO game_results (player_name, attempts, correct_guesses, time_spent)
            VALUES (?, ?, ?, ?)
        """,
            (player_name, attempts, correct_guesses, time_spent),
        )
        self.conn.commit()

    def fetch_all_results(self):
        self.cursor.execute("SELECT * FROM game_results")
        return self.cursor.fetchall()

    def drop_table(self):
        self.cursor.execute("DROP TABLE game_results")
