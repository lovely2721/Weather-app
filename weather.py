import requests

def get_weather(city):
    url = f"https://wttr.in/{city}?format=3"
    try:
        r = requests.get(url)
        print(r.text)
    except:
        print("Internet check karo yaar!")

city = input("City likho: ")
get_weather(city)import requests

def get_weather(city):
    url = f"https://wttr.in/{city}?format=3"
    try:
        r = requests.get(url)
        print(r.text)
    except:
        print("Internet check karo yaar!")

city = input("City likho: ")
get_weather(city)
