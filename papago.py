import requests
from decouple import config
import pprint

# 1. 네이버 API 설정
naver_client_id = config('NAVER_Client_ID')
naver_client_secret = config('NAVER_Client_Secret')
# 2. URL 설정
naver_url = 'https://openapi.naver.com/v1/papago/n2mt'
# 3. 요청보내기! POST
headers = { 'X-Naver-Client-Id' : naver_client_id,
        'X-Naver-Client-Secret' : naver_client_secret
}
data = {
    'source' : 'ko',
    'target' : 'en',
    'text' : '엄마판다는 새끼가 있네'
}


response = requests.post(naver_url, headers=headers, data=data).json()
pprint.pprint(response.get('message').get('result').get('translatedText'))
