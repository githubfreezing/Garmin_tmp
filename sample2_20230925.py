from datetime import date
from garminconnect import (
    Garmin,
    GarminConnectConnectionError,
    GarminConnectTooManyRequestsError,
    GarminConnectAuthenticationError,
)

email = "s.katsumata1988@gmail.com"
password = "Lemoned622"

# Garminへの接続を初期化
connect = Garmin(email, password)
connect.login()

# 今日の日付を取得
today = date.today().strftime('%Y-%m-%d')

# # アクティビティデータを取得
# activities = connect.get_activities(0,1)  # 最新の1つのアクティビティを取得]
# print("Activities:", activities)

# # ステップデータを取得
# steps = connect.get_steps_data(today)
# print("Steps:", steps)

# # 睡眠データを取得
# sleep = connect.get_sleep_data(today)
# print("Sleep:", sleep)

# # 体重データを取得
# weight = connect.get_weight_data(today)
# print("Weight:", weight)

# 心拍数データを取得
heart_rates = connect.get_heart_rates(today)
print("##########Heart Rates:##########")
print("Heart Rates:", heart_rates)

# # を取得
# blood_pressure = connect.get_blood_pressure(today)
# print("blood_pressure:", blood_pressure)






# try:
#     # Garminへの接続を初期化
#     connect = Garmin(email, password)
#     connect.login()

#     # 今日の日付を取得
#     today = date.today().strftime('%Y-%m-%d')

#     # 心拍数データを取得
#     heart_rates = connect.get_heart_rates(today)

#     print(heart_rates)

# except (
#     GarminConnectConnectionError,
#     GarminConnectAuthenticationError,
#     GarminConnectTooManyRequestsError,
# ) as err:
#     print(f"Error occurred during Garmin Connect Client init: {err}")
#     quit()