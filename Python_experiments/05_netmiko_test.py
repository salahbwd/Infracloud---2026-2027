import datetime
import netmiko
import paramiko
from netmiko import ConnectHandler
import platform
import subprocess

# Huidige datum en tijd weergeven
print("Huidige tijd:", datetime.datetime.now())
print("Paramiko versie:", paramiko.__version__)
print("Netmiko versie:", netmiko.__version__)


def get_serial_number():
    """Haalt het serienummer van de lokale computer op (voor Windows en Linux)."""
    try:
        if platform.system() == "Windows":
            cmd = "wmic bios get serialnumber"
            output = (
                subprocess.check_output(cmd, shell=True).decode().split("\n")
            )
            lines = [line.strip() for line in output if line.strip()]
            if len(lines) > 1:
                return lines[1]
        elif platform.system() == "Linux":
            with open("/sys/class/dmi/id/product_serial", "r") as f:
                return f.read().strip()
    except Exception:
        pass
    return "Onbekend"


# Sla het serienummer op in een dictionary
systeem_info = {
    "serienummer": get_serial_number()
}

print("Lokaal serienummer opgehaald:", systeem_info["serienummer"])

# Voorbeeld Netmiko verbindingsconfiguratie
device = {
    "device_type": "cisco_ios",
    "host": "10.10.20.48",
    "username": "developer",
    "password": "C1sco12345",
    "secret": "C1sco12345",
}

# Verwijder de commentaartekens (#) hieronder om de verbinding te starten wanneer je verbonden bent met het netwerk/VPN
# connection = ConnectHandler(**device)
# connection.enable()
# output = connection.send_command("show ip int brief")
# print(output)
# connection.disconnect()
