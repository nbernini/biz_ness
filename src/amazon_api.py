import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

def get_amazon_best_sellers(aws_access_key_id, aws_secret_access_key, search_term):
    client = boto3.client('advertising', 
                          aws_access_key_id=aws_access_key_id, 
                          aws_secret_access_key=aws_secret_access_key, 
                          region_name='us-east-1')
    try:
        response = client.search_items(Keywords=search_term, MarketplaceId='ATVPDKIKX0DER')
        return response
    except (NoCredentialsError, PartialCredentialsError):
        return "Invalid AWS credentials"

if __name__ == "__main__":
    aws_access_key_id = 'your_access_key_id'
    aws_secret_access_key = 'your_secret_access_key'
    search_term = "custom cutting boards"
    print(get_amazon_best_sellers(aws_access_key_id, aws_secret_access_key, search_term))
