"""
SQL Injection Vulnerability Example
====================================
EDUCATIONAL PURPOSE ONLY - DO NOT USE IN PRODUCTION

This script demonstrates SQL injection vulnerabilities where user input
is directly concatenated into SQL queries without sanitization.
"""

import sqlite3

# Vulnerable function - SQL Injection
def vulnerable_login(username, password):
    """
    VULNERABLE: User input is directly concatenated into SQL query.
    An attacker could input: username = "admin' --" to bypass authentication.
    """
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    
    # Create a sample users table
    cursor.execute('''CREATE TABLE users (id INTEGER, username TEXT, password TEXT)''')
    cursor.execute("INSERT INTO users VALUES (1, 'admin', 'secretpass123')")
    cursor.execute("INSERT INTO users VALUES (2, 'user', 'password456')")
    
    # VULNERABLE CODE - String concatenation in SQL
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    print(f"[VULNERABLE] Executing query: {query}")
    
    cursor.execute(query)
    result = cursor.fetchone()
    conn.close()
    
    return result is not None


def vulnerable_search(search_term):
    """
    VULNERABLE: Union-based SQL injection
    Attacker could use: "' UNION SELECT password FROM users --"
    """
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    
    cursor.execute('''CREATE TABLE products (id INTEGER, name TEXT, price REAL)''')
    cursor.execute("INSERT INTO products VALUES (1, 'Laptop', 999.99)")
    cursor.execute("INSERT INTO products VALUES (2, 'Mouse', 29.99)")
    
    # VULNERABLE CODE
    query = "SELECT * FROM products WHERE name LIKE '%" + search_term + "%'"
    print(f"[VULNERABLE] Executing query: {query}")
    
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    
    return results


# Example attacks
if __name__ == "__main__":
    print("=== SQL Injection Vulnerability Examples ===\n")
    
    # Attack 1: Authentication bypass
    print("1. Authentication Bypass Attack:")
    print("   Normal login: admin / wrongpassword")
    result = vulnerable_login("admin", "wrongpassword")
    print(f"   Login successful: {result}\n")
    
    print("   Attack login: admin' -- / anything")
    result = vulnerable_login("admin' --", "anything")
    print(f"   Login successful: {result}")
    print("   ^ Bypassed authentication!\n")
    
    # Attack 2: Union-based injection
    print("2. Union-Based SQL Injection:")
    print("   Normal search: Laptop")
    results = vulnerable_search("Laptop")
    print(f"   Results: {results}\n")
    
    print("   Attack search: ' UNION SELECT 999, 'HACKED', 0 --")
    results = vulnerable_search("' UNION SELECT 999, 'HACKED', 0 --")
    print(f"   Results: {results}")
    print("   ^ Injected malicious data!\n")
    
    print("\n=== SECURE ALTERNATIVE ===")
    print("Use parameterized queries:")
    print('cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))')
