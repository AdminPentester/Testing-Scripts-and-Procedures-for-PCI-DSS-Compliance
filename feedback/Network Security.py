import subprocess

def check_firewall_rules():
    try:
        result = subprocess.run(
            ["sudo", "iptables", "-L", "-v", "-n"],
            capture_output=True, text=True
        )
        return f"Firewall rules:\n{result.stdout}"
    except subprocess.CalledProcessError as e:
        return f"Error checking firewall rules: {e}"

def check_network_segmentation():
    try:
        interfaces = subprocess.run(["ip", "a"], capture_output=True, text=True)
        routing = subprocess.run(["ip", "route"], capture_output=True, text=True)
        return f"Network interfaces:\n{interfaces.stdout}\nRouting table:\n{routing.stdout}"
    except subprocess.CalledProcessError as e:
        return f"Error checking network segmentation: {e}"

# Example usage
print(check_firewall_rules())
print(check_network_segmentation())
