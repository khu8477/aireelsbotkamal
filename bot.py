import os
import requests

def get_latest_news():
    api_key = os.getenv("NEWS_API_KEY")
    # جلب أخبار كرة القدم من NewsAPI
    url = f"https://newsapi.org/v2/everything?q=football&apiKey={api_key}&language=ar&sortBy=publishedAt"
    
    response = requests.get(url).json()
    if response.get('articles'):
        return response['articles'][0] # جلب أحدث خبر
    return None

def post_to_facebook(news):
    page_id = os.getenv("FB_PAGE_ID")
    token = os.getenv("FB_TOKEN")
    url = f"https://graph.facebook.com/{page_id}/feed"
    
    payload = {
        'message': f"{news['title']}\n\n{news['description']}",
        'link': news['url'],
        'access_token': token
    }
    
    res = requests.post(url, data=payload)
    return res.status_code == 200

if __name__ == "__main__":
    news = get_latest_news()
    if news:
        if post_to_facebook(news):
            print("✅ تم النشر بنجاح")
        else:
            print("❌ فشل النشر")
    
