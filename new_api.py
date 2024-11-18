import requests

api_key = "4T%2F7SUOl0fRu%2BLWdKyc9LbyOW7ce%2BvKPKbuwHdH0wKjAUB9MiXa2Zhqx4OenMiAlGDDH%2BoCOOH59NG2DHObCig%3D%3D"
# 사용하려는 API URL (예시)
url = "https://api.odcloud.kr/api/15119893/v1/uddi:44e123dc-fb29-421a-996d-a0d3e14971ef"
# 헤더에 인증키를 추가

headers = {
    "Authorization": api_key
}
params = {
    "page": 1,
    "perPage": 10,
    "returnType": "JSON",
}

# 요청 보내기
response = requests.get(url, headers=headers, params=params)

# 응답 확인
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code}, {response.text}")