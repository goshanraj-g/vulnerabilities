# Security Vulnerabilities Examples - Educational Purposes Only

⚠️ **WARNING**: These scripts contain intentional security vulnerabilities for educational purposes. NEVER use this code in production or real applications.

## Vulnerability Categories

### 1. SQL Injection (`sql_injection.py`)
- Demonstrates unsanitized user input in SQL queries
- Shows how attackers can manipulate database queries

### 2. Cross-Site Scripting (XSS) (`xss_example.js`)
- Demonstrates reflected and stored XSS vulnerabilities
- Shows unsafe HTML rendering

### 3. Command Injection (`command_injection.py`)
- Demonstrates OS command injection vulnerabilities
- Shows unsafe use of system commands with user input

### 4. Path Traversal (`path_traversal.py`)
- Demonstrates directory traversal attacks
- Shows unsafe file path handling

### 5. Insecure Deserialization (`insecure_deserialization.py`)
- Demonstrates pickle vulnerability in Python
- Shows risks of deserializing untrusted data

### 6. XML External Entity (XXE) (`xxe_attack.py`)
- Demonstrates XXE injection vulnerabilities
- Shows unsafe XML parsing

### 7. Cross-Site Request Forgery (CSRF) (`csrf_example.html`)
- Demonstrates CSRF attack vectors
- Shows missing CSRF token validation

### 8. Hardcoded Credentials (`hardcoded_secrets.py`)
- Demonstrates credential exposure in source code
- Shows poor secret management practices

### 9. Weak Cryptography (`weak_crypto.py`)
- Demonstrates weak encryption and hashing
- Shows outdated cryptographic practices

### 10. Buffer Overflow (`buffer_overflow.c`)
- Demonstrates classic buffer overflow vulnerability
- Shows unsafe memory operations

### 11. Race Condition (`race_condition.py`)
- Demonstrates TOCTOU (Time-of-check to Time-of-use)
- Shows unsafe concurrent operations

### 12. Server-Side Request Forgery (SSRF) (`ssrf_vulnerability.py`)
- Demonstrates SSRF attacks
- Shows unsafe URL fetching

### 13. LDAP Injection (`ldap_injection.py`)
- Demonstrates LDAP query manipulation
- Shows unsafe LDAP filter construction

### 14. Insecure Direct Object Reference (`idor_example.py`)
- Demonstrates IDOR vulnerabilities
- Shows missing authorization checks

## How to Use

Each file contains:
- Comments explaining the vulnerability
- Example vulnerable code
- Potential attack vectors
- Suggestions for secure alternatives

## Disclaimer

These examples are for educational purposes only. Understanding vulnerabilities helps developers write more secure code. Always follow security best practices in real applications.
