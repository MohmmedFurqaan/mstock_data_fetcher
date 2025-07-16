import requests
from config.config import API_KEY, PRIVATE_KEY
from utils._token import get_access_token


def fetch_historical_data(symbol="TCS", interval="1d", range_="1mo"): # setted the default Parameters if no company provided
    """
    Fetch historical market data from mStock API.
    """
    access_token = get_access_token()
    if not access_token:
        print("Cannot proceed without access token.")
        return

    url = "https://api.mstock.trade/v1/marketdata/historical"  # Confirm with actual API docs

    headers = {
        "Authorization": f"token {API_KEY}:{access_token}",
        "X-Mirae-Version": "1",
        "Content-Type": "application/json",
        "X-PrivateKey": PRIVATE_KEY
    }

    params = {
        "symbol": symbol,
        "interval": interval,
        "range": range_
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print("❌ Error fetching data:", e)
        return None

    if response.status_code == 200:
        data = response.json()
        print("✅ Historical data fetched successfully.")
        return data
    else:
        print(f"❌ API returned status {response.status_code}")
        print(response.text)
        return None


if __name__ == "__main__":
    # replace the symbols as per your requirnments .... as i don't know which stock u want
    result = fetch_historical_data(symbol="TCS", interval="1d", range_="1mo")
    if result:
        print(result)
