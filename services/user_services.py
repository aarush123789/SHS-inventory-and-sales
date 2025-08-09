import hashlib
from config.db import get_connection

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(username, email, password, contactno, address):
    conn = get_connection()
    cursor = conn.cursor()
    hashPassword = hash_password(password)
    print('hash password :', hashPassword)
    try:
        cursor.execute("""
            INSERT INTO users (username, email, password, contactno, address)
            VALUES (%s, %s, %s, %s, %s)
        """, (username, email, hashPassword, contactno, address))
        conn.commit()
        print(f"User {username} registered successfully.")
        return True
    except Exception as e:
        print("Registration error:", e)
        return False
    finally:
        print("Closing database connection.")
        conn.close()

def login_user(username, password):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        hashPassword = hash_password(password)
        cursor.execute("""
            SELECT * FROM users WHERE email=%s AND password=%s
        """, (username, hashPassword))
    
        user = cursor.fetchone()
        if user is None:
            print("User not found.")
            return False
        conn.close()
        return user
    except Exception as e:
        print("Login failed error:", e)
        return False
    
