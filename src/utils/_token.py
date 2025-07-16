import requests
from config.config import API_KEY, USERNAME, PASSWORD, PRIVATE_KEY

def get_access_token():
    """
    Generate an access token using mStock API credentials.
    """
    url = "https://api.mstock.trade/auth/login"  # url for the Mstock

    headers = {
        "Content-Type": "application/json",
        "X-Mirae-Version": "1",
        "X-PrivateKey": PRIVATE_KEY
    }

    payload = {
        "username": USERNAME,
        "password": PASSWORD,
        "apiKey": API_KEY
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print("❌ Error connecting to mStock:", e)
        return None

    if response.status_code == 200:
        data = response.json()
        access_token = data.get("accessToken")
        if access_token:
            print("✅ Access Token generated successfully.")
            return access_token
        else:
            print("❌ Access token not found in response.")
            print(data)
            return None
    else:
        print(f"❌ Failed with status code {response.status_code}:")
        print(response.text)
        return None
