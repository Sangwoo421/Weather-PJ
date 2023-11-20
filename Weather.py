import streamlit as st
from PIL import Image
import io
import os
import random

# 사용자로부터 온도 입력 받기
temperature = st.number_input("현재 기온을 입력하세요", min_value=-10.0, max_value=40.0, step=0.1)

st.header("Streamlit 옷 추천")

# 현재 기온에 따라 이미지 선택
if st.button("추천"):
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
    st.image(image, caption=f"현재 기온: {temperature}도 (추천)", use_column_width=True)

