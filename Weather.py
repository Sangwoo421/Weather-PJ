import streamlit as st
import requests
from PIL import Image
import io
import os
from datetime import datetime
import random

# 대한민국 기상청 API 키
api_key = "2u0%2FXKU8a2RYIHnZ9ZNMGTi2PuzLlvbjSv7TVb2kYK2CM1EVfy%2FfcrNzFYznuB8s7%2FNGnYNA%2FWrYFvhWwXO0%2Bg%3D%3D"

# API URL
url = "http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst"

# API 키 디코딩
api_key_decoded = requests.utils.unquote(api_key, 'UTF-8')

# 현재 날짜와 시간
now = datetime.now()
base_date = now.strftime("%Y%m%d")
base_time = now.strftime("%H00")

# 현재 시간의 분을 가져옴
current_minute = int(now.strftime("%M"))

# 지역 정보
nx = "91"
ny = "106"

# 쿼리 파라미터 설정
params = {
    "serviceKey": api_key_decoded,
    "dataType": "JSON",
    "base_date": base_date,
    "base_time": base_time,
    "nx": nx,
    "ny": ny
}

try:    
    # API 요청 보내기
    response = requests.get(url, params=params)
    response.raise_for_status()
     # JSON 데이터 가져오기
    json_data = response.json()

    # 원하는 날씨 정보 추출 (기온, 강수형태, 풍속)
    temperature = float(json_data['response']['body']['items']['item'][0]['obsrValue'])
    precipitation_type = int(json_data['response']['body']['items']['item'][1]['obsrValue'])

    # Streamlit 앱에 날씨 정보 표시
    st.title("날씨 정보")
    st.write(f"현재 기온: {temperature}도")
    st.write(f"강수 형태: {precipitation_type} (0: 없음, 1: 비, 2: 비/눈, 3: 눈, 4: 소나기)")

    # 현재 기온이 5도 이하인 경우에만 이미지 표시
    if st.button("추천"):
        if temperature <= 5:
            # 이미지 파일 경로 (상대 경로 사용)
            image_directory = os.path.join(os.path.dirname(__file__), "5")
            image_files = [f for f in os.listdir(image_directory) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
            random_image_path = os.path.join(image_directory, random.choice(image_files))

            # 이미지를 바이너리로 읽기
            image_data = open(random_image_path, "rb").read()

            # 바이너리 이미지 데이터를 Image 객체로 변환
            image = Image.open(io.BytesIO(image_data))

            # Streamlit 앱에 이미지 표시
            st.image(image, caption=f"현재 기온: {temperature}도 (추천)", use_column_width=True)

        elif 6 <= temperature <= 15:
            # 이미지 파일 경로 (상대 경로 사용)
            image_directory = os.path.join(os.path.dirname(__file__), "15")
            image_files = [f for f in os.listdir(image_directory) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
            random_image_path = os.path.join(image_directory, random.choice(image_files))

            # 이미지를 바이너리로 읽기
            image_data = open(random_image_path, "rb").read()

            # 바이너리 이미지 데이터를 Image 객체로 변환
            image = Image.open(io.BytesIO(image_data))

            # Streamlit 앱에 이미지 표시
            st.image(image, caption=f"현재 기온: {temperature}도 (추천)", use_column_width=True)

        elif 16 <= temperature <= 23:
            # 이미지 파일 경로 (상대 경로 사용)
            image_directory = os.path.join(os.path.dirname(__file__), "23")
            image_files = [f for f in os.listdir(image_directory) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
            random_image_path = os.path.join(image_directory, random.choice(image_files))

            # 이미지를 바이너리로 읽기
            image_data = open(random_image_path, "rb").read()

            # 바이너리 이미지 데이터를 Image 객체로 변환
            image = Image.open(io.BytesIO(image_data))

            # Streamlit 앱에 이미지 표시
            st.image(image, caption=f"현재 기온: {temperature}도 (추천)", use_column_width=True)

        else:
            # 이미지 파일 경로 (상대 경로 사용)
            image_directory = os.path.join(os.path.dirname(__file__), "30")
            image_files = [f for f in os.listdir(image_directory) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
            random_image_path = os.path.join(image_directory, random.choice(image_files))

            # 이미지를 바이너리로 읽기
            image_data = open(random_image_path, "rb").read()

            # 바이너리 이미지 데이터를 Image 객체로 변환
            image = Image.open(io.BytesIO(image_data))

            # Streamlit 앱에 이미지 표시
            st.image(image, caption=f"현재 기온: {temperature}도 (추천)", use_column_width=True)

except Exception as e:
    st.error(f"오류 발생: {e}")
