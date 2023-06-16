import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_URL = 'https://fake-api-vycpfa6oca-uc.a.run.app/sales'
AUTH_TOKEN = os.getenv('AUTH_TOKEN')


def get_sales_data(date_str: str, page: int) -> dict:
    headers = {
        'Authorization': AUTH_TOKEN
    }
    params = {
        'date': date_str,
        'page': page
    }
    response = requests.get(API_URL, headers=headers, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        return {}




