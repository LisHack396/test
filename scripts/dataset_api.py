import requests
from requests import exceptions

def get_api_data(place = ''):
    if type(place) != str or not place.isalpha():
        raise ValueError(f"{place} is not defined")
    if place != '':
        url = f"https://www.worldweatheronline.com/{place}-weather.aspx"
    url = "https://www.worldweatheronline.com/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebkit/537.36 (KHTML, like Gecko) "
                        "Chrome/107.0.0.0 Safari/537.36"
    }
    try:
        response = requests.get(url, headers=headers, timeout=2.50)
        response.raise_for_status()
    except exceptions.HTTPError as http_error:
        print(f"HTTP error occured: {http_error}")
    except exceptions.ConnectionError as connecting_error:
        print(f"Connecting error occurred: {connecting_error}")
    except exceptions.Timeout as timeout_error:
        print(f"Timeout error occurred: {timeout_error}")
    except Exception as error:
        print(f"Error occurred: {error}")
    else:
        return response.json()

data = get_api_data('Jatibonico')
print(data)