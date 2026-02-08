"""
Path Traversal Vulnerability Example
=====================================
EDUCATIONAL PURPOSE ONLY - DO NOT USE IN PRODUCTION

This script demonstrates path traversal vulnerabilities where user input
can manipulate file paths to access unauthorized files.
"""

import os

# Base directory for "safe" file access
BASE_DIR = "./user_files/"

# VULNERABLE: Direct path concatenation
def vulnerable_read_file(filename):
    """
    VULNERABLE: No validation of user-provided filename
    Attack: "../../etc/passwd" or "..\\..\\windows\\system32\\config\\sam"
    """
    filepath = BASE_DIR + filename
    print(f"[VULNERABLE] Reading file: {filepath}")
    
    try:
        with open(filepath, 'r') as f:
            content = f.read()
        return content
    except Exception as e:
        return f"Error: {e}"


def vulnerable_file_download(file_path):
    """
    VULNERABLE: URL parameter used directly in file path
    Attack: "/download?file=../../../../etc/shadow"
    """
    print(f"[VULNERABLE] Downloading file: {file_path}")
    
    # VULNERABLE CODE - no path validation
    full_path = os.path.join(BASE_DIR, file_path)
    print(f"Full path: {full_path}")
    
    if os.path.exists(full_path):
        with open(full_path, 'rb') as f:
            return f.read()
    return None


def vulnerable_include_file(template_name):
    """
    VULNERABLE: Template inclusion without validation
    Attack: "../../../../etc/passwd%00" (null byte injection)
    """
    template_dir = "./templates/"
    template_path = template_dir + template_name + ".html"
    
    print(f"[VULNERABLE] Including template: {template_path}")
    
    # VULNERABLE CODE
    try:
        with open(template_path, 'r') as f:
            return f.read()
    except Exception as e:
        return f"Error: {e}"


def vulnerable_delete_file(filename):
    """
    VULNERABLE: File deletion with path traversal
    Attack: "../../../important_system_file.conf"
    """
    filepath = os.path.join("./uploads/", filename)
    print(f"[VULNERABLE] Deleting file: {filepath}")
    
    # VULNERABLE CODE - no validation before deletion
    if os.path.exists(filepath):
        os.remove(filepath)
        return "File deleted"
    return "File not found"


def vulnerable_list_directory(directory):
    """
    VULNERABLE: Directory listing without validation
    Attack: "../../" to list parent directories
    """
    base = "./public/"
    path = base + directory
    
    print(f"[VULNERABLE] Listing directory: {path}")
    
    # VULNERABLE CODE
    try:
        files = os.listdir(path)
        return files
    except Exception as e:
        return f"Error: {e}"


# Example attacks
if __name__ == "__main__":
    print("=== Path Traversal Vulnerability Examples ===\n")
    
    print("1. Directory Traversal Attack Vectors:")
    attack_vectors = [
        "../../../etc/passwd",              # Unix
        "..\\..\\..\\windows\\win.ini",     # Windows
        "....//....//....//etc/passwd",     # Double encoding
        "..%2F..%2F..%2Fetc%2Fpasswd",     # URL encoding
        "..%252F..%252Fetc%252Fpasswd",    # Double URL encoding
        "..///..///..///etc/passwd",        # Mixed separators
        "..%00.jpg",                         # Null byte injection
    ]
    
    for vector in attack_vectors:
        print(f"   - {vector}")
    
    print("\n2. Demonstrating Path Traversal:")
    print("   Normal input: document.txt")
    print("   Attack input: ../../sensitive_file.txt\n")
    
    # Show how the path would be constructed
    normal = os.path.join(BASE_DIR, "document.txt")
    attack = os.path.join(BASE_DIR, "../../sensitive_file.txt")
    
    print(f"   Normal path: {normal}")
    print(f"   Attack path: {attack}")
    print(f"   Normalized: {os.path.normpath(attack)}")
    
    print("\n3. Common Target Files:")
    targets = {
        "Unix/Linux": [
            "/etc/passwd",
            "/etc/shadow",
            "/root/.ssh/id_rsa",
            "/var/log/apache2/access.log",
            "~/.bash_history"
        ],
        "Windows": [
            "C:\\windows\\win.ini",
            "C:\\windows\\system32\\config\\sam",
            "C:\\boot.ini",
            "C:\\windows\\repair\\sam"
        ]
    }
    
    for os_type, files in targets.items():
        print(f"\n   {os_type}:")
        for file in files:
            print(f"      - {file}")
    
    print("\n=== SECURE ALTERNATIVES ===")
    print("""
1. Use os.path.realpath() to resolve the actual path
2. Validate that resolved path is within allowed directory
3. Use allowlist of permitted filenames
4. Remove all directory traversal sequences
5. Use os.path.basename() for filenames only
    
SECURE EXAMPLE:

def secure_read_file(filename):
    '''SECURE: Validates path is within allowed directory'''
    # Get absolute path of base directory
    base_dir = os.path.realpath(BASE_DIR)
    
    # Construct and resolve the full path
    requested_path = os.path.realpath(os.path.join(base_dir, filename))
    
    # Verify the path is within base directory
    if not requested_path.startswith(base_dir):
        raise ValueError("Access denied: Path traversal detected")
    
    # Additional validation
    if '..' in filename or filename.startswith('/'):
        raise ValueError("Invalid filename")
    
    with open(requested_path, 'r') as f:
        return f.read()
    """)
    
    print("\n4. Defense in Depth:")
    print("   - Run application with minimal privileges")
    print("   - Use chroot jails or containers")
    print("   - Implement file access logging")
    print("   - Use WAF (Web Application Firewall) rules")
