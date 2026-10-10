import datetime
import json
import platform
import subprocess
import requests
import sys

# --- Serienummer ophalen functie (Opdracht 8) ---
def get_serial_number():
    """Haalt het serienummer van de computer op (voor Windows en Linux)."""
    try:
        if platform.system() == "Windows":
            cmd = "wmic bios get serialnumber"
            output = subprocess.check_output(cmd, shell=True).decode().split("\n")
            lines = [line.strip() for line in output if line.strip()]
            if len(lines) > 1:
                return lines[1]
        elif platform.system() == "Linux":
            with open("/sys/class/dmi/id/product_serial", "r") as f:
                return f.read().strip()
    except Exception:
        pass
    return "Onbekend"

# Serienummer opslaan in een dictionary
systeem_info = {
    "serienummer": get_serial_number()
}
print("Serienummer van de PC:", systeem_info["serienummer"])

# --- Subnet Masker Hulpfuncties ---
netmask_prefixes = {
    '255.255.255.255': '/32', '255.255.255.254': '/31', '255.255.255.252': '/30',
    '255.255.255.248': '/29', '255.255.255.240': '/28', '255.255.255.224': '/27',
    '255.255.255.192': '/26', '255.255.255.128': '/25', '255.255.255.0': '/24'
}

def get_net_prefix(p_subnet_mask):
    return netmask_prefixes.get(p_subnet_mask, "Verkeerde invoer")

def get_number_ip_hosts(p_prefix):
    pbits = 32 - int(p_prefix[1:])
    return (2 ** pbits) - 2

print("Subnet test /27:", get_number_ip_hosts('/27'), "hosts")

# --- Mijn IP-adres ophalen ---
now = datetime.datetime.now()
print("\nHuidige tijd:", now)

try:
    r = requests.get("https://api.ipify.org?format=json", timeout=10)
    if r.status_code == 200:
        ip_json = r.json()
        print("JSON-antwoord:", json.dumps(ip_json))
        print("IP-adres:", ip_json.get("ip"))
    else:
        print("Fout bij het ophalen van IP:", r.status_code)
except Exception as e:
    print("Aanvraag mislukt:", e)
