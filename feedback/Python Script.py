import subprocess

def check_tls_version(ip):
    try:
        result = subprocess.run(
            ["nmap", "--script", "ssl-enum-ciphers", "-p", "443", ip],
            capture_output=True, text=True, check=True
        )
        output = result.stdout
        if "TLSv1.2" in output or "TLSv1.3" in output:
            return "TLS 1.2 or higher is supported."
        else:
            return "Outdated TLS versions detected."
    except subprocess.CalledProcessError as e:
        return f"Error checking TLS version: {e}"

def check_encryption_on_storage():
    try:
        result = subprocess.run(
            ["lsblk", "-f"],
            capture_output=True, text=True, check=True
        )
        output = result.stdout
        if "crypto" in output:
            return "Encryption detected on storage."
        else:
            return "No encryption detected on storage."
    except subprocess.CalledProcessError as e:
        return f"Error checking encryption on storage: {e}"

# Example usage
ip_address = '192.168.1.1'
print(check_tls_version(ip_address))
print(check_encryption_on_storage())
