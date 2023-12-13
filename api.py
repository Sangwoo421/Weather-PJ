import requests
from datetime import datetime
import xml.etree.ElementTree as ET

url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtFcst'
servicekey = '2u0/XKU8a2RYIHnZ9ZNMGTi2PuzLlvbjSv7TVb2kYK2CM1EVfy/fcrNzFYznuB8s7/NGnYNA/WrYFvhWwXO0+g=='

now = datetime.now()
base_date = now.strftime("%Y%m%d")

params ={'serviceKey' : servicekey, 'pageNo' : '1', 'numOfRows' : '1000', 'dataType' : 'XML', 'base_date' : base_date, 'base_time' : '1930', 'nx' : '91', 'ny' : '106' }

response = requests.get(url, params=params)

root = ET.fromstring(response.content)

last_temperature = None
for item in root.findall(".//item[category='T1H']"):
    fcst_value = item.find("fcstValue").text
    last_temperature = fcst_value

if last_temperature is not None:
    print(f"예보 온도: {last_temperature}°C")
else:
    print("온도 정보를 찾을 수 없습니다.")
