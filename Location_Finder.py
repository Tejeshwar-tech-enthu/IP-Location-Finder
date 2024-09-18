import requests

def get_location_by_ip(ip_address):
    try:
        response = requests.get(f"https://ipinfo.io/{ip_address}/json")
        data = response.json()
        
        location_info = {
            "IP Address": data.get("ip"),
            "Region": data.get("region"),
            "Country": data.get("country"),
            "Location": data.get("loc"),  
        }
        
        return location_info
    except Exception:
        return {"error": str(Exception)}


ip_address = requests.get("https://api.ipify.org").text
location = get_location_by_ip(ip_address)
print(location)
