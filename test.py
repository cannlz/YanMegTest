import sqlite3 as sq
baseMain = sq.connect('megmark.db', check_same_thread = False)
proxy = baseMain.execute(f'SELECT proxy FROM users WHERE user_id = 407073449').fetchone()
print(proxy[0])