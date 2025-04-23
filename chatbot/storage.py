import sqlite3
import os

def init_db():
    os.makedirs("data", exist_ok=True)
    conn = sqlite3.connect("data/conversations.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS chats 
                 (timestamp TEXT, module TEXT, user_input TEXT, bot_response TEXT, sentiment TEXT)''')
    conn.commit()
    conn.close()

def save_chat(module, user_input, bot_response, sentiment):
    conn = sqlite3.connect("data/conversations.db")
    c = conn.cursor()
    c.execute("INSERT INTO chats VALUES (datetime('now'), ?, ?, ?, ?)", 
              (module, user_input, bot_response, sentiment))
    conn.commit()
    conn.close()
