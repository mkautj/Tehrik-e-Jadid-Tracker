# database.py
import sqlite3

def init_db():
    conn = sqlite3.connect('tehrik_jadid.db')
    c = conn.cursor()
    
    # Form I Table
    c.execute('''CREATE TABLE IF NOT EXISTS form_i (
        id INTEGER PRIMARY KEY,
        financial_year TEXT,
        month TEXT,
        total_promises INTEGER,
        amount_paid REAL,
        balance REAL,
        book_no TEXT UNIQUE,
        receipt_no TEXT UNIQUE,
        son_of TEXT,
        qiadat_secretary TEXT,
        synced INTEGER DEFAULT 0  # 0 = unsynced, 1 = synced
    )''')
    
    # Form II Table (similar structure)
    c.execute('''CREATE TABLE IF NOT EXISTS form_ii (
        id INTEGER PRIMARY KEY,
        financial_year TEXT,
        month TEXT,
        total_promises INTEGER,
        amount_paid REAL,
        balance REAL,
        book_no TEXT UNIQUE,
        receipt_no TEXT UNIQUE,
        son_of TEXT,
        qiadat_secretary TEXT,
        synced INTEGER DEFAULT 0  # 0 = unsynced, 1 = synced
    )''')
    
    conn.commit()
    conn.close()

# Initialize the database
init_db()