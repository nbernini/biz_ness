import requests

def search_etsy(api_key, search_term):
    response = requests.get(f'https://openapi.etsy.com/v2/listings/active?keywords={search_term}&api_key={api_key}')
    return response.json()

if __name__ == "__main__":
    api_key = 'your_api_key'
    search_term = "custom cutting boards"
    print(search_etsy(api_key, search_term))
