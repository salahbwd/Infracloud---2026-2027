import datetime
import platform
import subprocess

# Huidige datum en tijd weergeven
now = datetime.datetime.now()
print("Huidige datum en tijd:")
print(now)


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


# Dictionary (woordenboek) voor Opdracht 8 met het serienummer
mijn_pc = {"serienummer": get_serial_number()}

print("Resultaat Opdracht 8 (Serienummer):")
print(mijn_pc)
