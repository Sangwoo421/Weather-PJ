from datetime import datetime

# 현재 날짜를 얻어옴
now = datetime.now()
current_date = now.date()
current_time = now.time()

print(current_date)
print(current_time)