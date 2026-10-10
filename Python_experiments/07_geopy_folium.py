import datetime
import platform
import subprocess
from geopy.geocoders import Nominatim
import folium

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

# Serienummer opslaan in een dictionary
systeem_info = {
    "serienummer": get_serial_number()
}
print("Serienummer van de PC:", systeem_info["serienummer"])

# Geopy en Folium gedeelte
geolocator = Nominatim(user_agent="http://biasc.be")
city_country = "Kyiv, Ukraine"

location = geolocator.geocode(city_country)
print("Adres:", location.address)
devnet_lat = location.latitude
devnet_lon = location.longitude
print("Coördinaten:", (devnet_lat, devnet_lon))

coordinates = [devnet_lat, devnet_lon]
map_obj = folium.Map(location=coordinates, tiles='OpenStreetMap', zoom_start=12)
map_obj.save("geopy_location.html")
print("Kaart opgeslagen als geopy_location.html")
