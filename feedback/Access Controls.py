import subprocess

def check_mfa_installed():
    try:
        result = subprocess.run(
            ["grep", "'auth required pam_google_authenticator.so'", "/etc/pam.d/sshd"],
            capture_output=True, text=True
        )
        if result.stdout:
            return "MFA is configured."
        else:
            return "MFA is not configured."
    except subprocess.CalledProcessError as e:
        return f"Error checking MFA configuration: {e}"

def list_users_and_groups():
    try:
        users = subprocess.run(["cat", "/etc/passwd"], capture_output=True, text=True)
        groups = subprocess.run(["cat", "/etc/group"], capture_output=True, text=True)
        return f"Users:\n{users.stdout}\nGroups:\n{groups.stdout}"
    except subprocess.CalledProcessError as e:
        return f"Error listing users and groups: {e}"

# Example usage
print(check_mfa_installed())
print(list_users_and_groups())
