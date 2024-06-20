from google_trends import get_google_trends
from etsy_api import search_etsy
from amazon_api import get_amazon_best_sellers

def main():
    # Google Trends
    keywords = ["custom cutting boards", "3D printed toys"]
    google_trends_data = get_google_trends(keywords)
    print("Google Trends Data:", google_trends_data)
    
    # Etsy API
    etsy_api_key = 'your_etsy_api_key'
    etsy_search_term = 'custom cutting boards'
    etsy_data = search_etsy(etsy_api_key, etsy_search_term)
    print("Etsy Data:", etsy_data)
    
    # Amazon API
    aws_access_key_id = 'your_access_key_id'
    aws_secret_access_key = 'your_secret_access_key'
    amazon_search_term = 'custom cutting boards'
    amazon_data = get_amazon_best_sellers(aws_access_key_id, aws_secret_access_key, amazon_search_term)
    print("Amazon Data:", amazon_data)

if __name__ == "__main__":
    main()


