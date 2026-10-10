import json
import platform
import subprocess

# Serienummer ophalen functie (Opdracht 8)
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

if_dict = {
    "ietf-interfaces:interfaces": {
        "interface": [
            {
                "name": "GigabitEthernet1",
                "description": "VBox",
                "type": "iana-if-type:ethernetCsmacd",
                "enabled": True,
                "ietf-ip:ipv4": {"address": [{"ip": "192.168.56.101", "netmask": "255.255.255.0"}]},
                "ietf-ip:ipv6": {}
            },
            {
                "name": "Loopback9",
                "description": "999",
                "type": "iana-if-type:softwareLoopback",
                "enabled": True,
                "ietf-ip:ipv4": {"address": [
                    {"ip": "10.9.9.9", "netmask": "255.255.255.0"},
                    {"ip": "172.29.0.9", "netmask": "255.255.255.0"}
                ]},
                "ietf-ip:ipv6": {}
            }
        ]
    },
    # Serienummer automatisch toegevoegd aan de dictionary
    "serienummer": get_serial_number()
}

print("Type van if_dict:", type(if_dict))
print(if_dict)

# Converteer Dictionary naar JSON-string
if_json = json.dumps(if_dict, indent=2)
print("\nGeformatteerde JSON-string:")
print(if_json)
print("Type van if_json:", type(if_json))
