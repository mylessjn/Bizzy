import sqlite3
import csv
from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"


def get_conn(folder):
    ""Open/create folder and return the connection""
    db_path = DATA_DIR / folder / "bizzy.db"
    sqlite3.connect("db_path")
    conn.row_factory = sqlite3.Row
    conn.execute("Pragma foreign_keys = ON")
    return conn

def init_db(folder):

    conn = get_conn(folder) # connect to the folder

    conn.execute("""
        CREATE TABLE IF NOT EXISTS inventory (
        ingredient TEXT PRIMARY KEY,
        unit TEXT,
        price REAL,
        current_qty REAL,
        reorder_point REAL,
        reorder_qty REAL,
        supplier TEXT
        )
        """)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS menu (
        menu_item TEXT PRIMARY KEY,
        price REAL
        )
        """)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS sales(
        id INTEGER PRIMARY KEY,
        order_time TEXT,
        menu_item TEXT,
        qty REAL
        )
        """)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS orders(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date_and_time TEXT,
        ingredient TEXT,
        qty REAL,
        supplier TEXT,
        status TEXT
        )
        """)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS recipes(
        menu_item TEXT,
        qty_used REAL,
        ingredient TEXT,
        PRIMARY KEY(menu_item, ingredient)
        )
        """)
    
    conn.commit()
    conn.close()
    
    

if __name__ == "__main__":
    import sys
    setup(sys.argv[1])