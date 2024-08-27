import ssl
import socket
import subprocess

def check_tls_version(ip):
    context = ssl.create_default_context()
    with socket.create_connection((ip, 443)) as sock:
        with context.wrap_socket(sock, server_hostname=ip) as ssock:
            tls_version = ssock.version()
            if tls_version in ['TLSv1.2', 'TLSv1.3']:
                return f"Supported TLS version: {tls_version}"
            else:
                return "Outdated TLS version detected."

def check_encryption_on_storage():
    try:
        result = subprocess.run(
            ["lsblk", "-o", "NAME,TYPE,FSTYPE,MOUNTPOINT,UUID"],
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
