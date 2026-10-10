import datetime
import json
import platform
import psutil
import socket
import subprocess


def get_serial_number():
    """Haalt het serienummer van de computer op (voor Windows en Linux)."""
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


def collect_system_info():
    data = {}

    # Serienummer toevoegen aan de gegevens (Opdracht 8)
    data["serienummer"] = get_serial_number()

    # CPU-informatie
    data["cpu"] = {
        "platform": platform.platform(),
        "processor": platform.processor(),
        "physical_cores": psutil.cpu_count(logical=False),
        "logical_processors": psutil.cpu_count(logical=True),
        "cpu_percent_total": psutil.cpu_percent(interval=0.1),
    }

    # Geheugen-informatie
    data["memory"] = psutil.virtual_memory()._asdict()

    # Netwerk hostname en FQDN
    data["network"] = {
        "hostname": socket.gethostname(),
        "fqdn": socket.getfqdn(),
    }

    return data


if __name__ == "__main__":
    print("Uitvoeringstijd:", datetime.datetime.now())
    info = collect_system_info()
    print(json.dumps(info, indent=2))
