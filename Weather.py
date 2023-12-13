import streamlit as st
from PIL import Image
import io
import os
import random
import requests
from datetime import datetime
import xml.etree.ElementTree as ET

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://i.imgur.com/zRtWHdz.jpg");
             background-attachment: fixed;
             background-size: cover
             
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()

st.header("𝑻𝒆𝒎𝒑𝒆𝒓𝒂𝒕𝒆 𝑻𝒓𝒆𝒏𝒅𝒔")
subheader = st.text("𝙋𝙡𝙚𝙖𝙨𝙚 𝙚𝙣𝙩𝙚𝙧 𝙩𝙝𝙚 𝙘𝙪𝙧𝙧𝙚𝙣𝙩 𝙩𝙚𝙢𝙥𝙚𝙧𝙖𝙩𝙪𝙧𝙚")

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

# 사용자로부터 온도 입력 받기
temperature = st.number_input("𝘛𝘦𝘮𝘱𝘦𝘳𝘢𝘵𝘶𝘳𝘦", min_value=-10, max_value=40, step=1)

# 현재 기온에 따라 이미지 선택
if st.button("RECOMMEND"):
    if temperature <= 5:
        image_directory = os.path.join(os.path.dirname(__file__), "5")
    elif 6 <= temperature <= 15:
        image_directory = os.path.join(os.path.dirname(__file__), "15")
    elif 16 <= temperature <= 23:
        image_directory = os.path.join(os.path.dirname(__file__), "23")
    else:
        image_directory = os.path.join(os.path.dirname(__file__), "30")

    image_files = [f for f in os.listdir(image_directory) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    random_image_path = os.path.join(image_directory, random.choice(image_files))

    # 이미지를 바이너리로 읽기
    image_data = open(random_image_path, "rb").read()

    # 바이너리 이미지 데이터를 Image 객체로 변환
    image = Image.open(io.BytesIO(image_data))

    # Streamlit 앱에 이미지 표시
    st.image(image, caption=f"기온: {last_temperature}도 (추천)", use_column_width=True)