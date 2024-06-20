from pytrends.request import TrendReq

def get_google_trends(keywords):
    pytrends = TrendReq(hl='en-US', tz=360)
    pytrends.build_payload(keywords, cat=0, timeframe='today 12-m', geo='', gprop='')
    return pytrends.interest_over_time()

if __name__ == "__main__":
    keywords = ["custom cutting boards", "3D printed toys"]
    print(get_google_trends(keywords))
