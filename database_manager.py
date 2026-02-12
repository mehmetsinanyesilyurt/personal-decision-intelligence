import sqlite3
from datetime import datetime

class DatabaseManager:
    def __init__(self, db_name="sentinel_data.db"):
        self.db_name = db_name
        self.init_db()

    def init_db(self):
        """Tabloları kurumsal standartta oluşturur."""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            # Karar Takip Tablosu
            cursor.execute('''CREATE TABLE IF NOT EXISTS decisions (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                date TEXT,
                                category TEXT,
                                decision_text TEXT,
                                expected_outcome TEXT,
                                reality_score INTEGER DEFAULT 0,
                                risk_level TEXT)''')
            
            # Sistem Log Tablosu (Risk analizi için)
            cursor.execute('''CREATE TABLE IF NOT EXISTS system_logs (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                timestamp TEXT,
                                cpu_usage REAL,
                                ram_usage REAL,
                                alert_triggered BOOLEAN)''')
            conn.commit()

    def add_decision(self, category, text, outcome, risk):
        with sqlite3.connect(self.db_name) as conn:
            curr = conn.cursor()
            curr.execute("INSERT INTO decisions (date, category, decision_text, expected_outcome, risk_level) VALUES (?,?,?,?,?)",
                         (datetime.now().strftime("%Y-%m-%d %H:%M"), category, text, outcome, risk))
            conn.commit()

    def log_system(self, cpu, ram, alert):
        with sqlite3.connect(self.db_name) as conn:
            curr = conn.cursor()
            curr.execute("INSERT INTO system_logs (timestamp, cpu_usage, ram_usage, alert_triggered) VALUES (?,?,?,?)",
                         (datetime.now().strftime("%H:%M:%S"), cpu, ram, alert))
