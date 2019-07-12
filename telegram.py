import requests
import pprint
from decouple import config #파이썬에서 환경변수 관리하는 패키지

# 1. 토큰 및 기본 url 설정
#token = config('TELEGRAM_TOKEN') # .env 설정값 가져오기
token = '724381298:AAHO2F-mn3Hbf13vgWgcWYYT2QFJYuXdifM'
base_url = f"https://api.telegram.org/bot{token}/"

# 2. getUpdates 정보 가져오기
response = requests.get(base_url + 'getUpdates').json()
#pprint.pprint(response)

# 3. 나의 chat_id 가져오기
chat_id = response['result'][0]['message']['chat']['id']
print(chat_id)
# 757095439

# 4. chat_id에 메세지 보내기
# 4-1. 요청 보낼 URL 만들기
text = '안녕?'
api_url = f'{base_url}sendMessage?chat_id={chat_id}&text={text}'
# 4-2. requests로 보내기
requests.get(api_url)
#sendMessage?chat_id=757095439&text=너는%20안녕하니