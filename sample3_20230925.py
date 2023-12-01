from garminconnect import Garmin
from datetime import datetime, timedelta

# # Garmin Connectのユーザー名とパスワードを設定
# email = "s.katsumata1988@gmail.com"
# password = "Lemoned622"

# api = Garmin('s.katsumata1988@gmail.com', 'Lemoned622')
# #api = Garmin('mtk.ms-590708@docomone.jp', 'Basuke0829')
email = "mtk.ms-590708@docomo.ne.jp"
password = "Basuke0829"

# Garminオブジェクトを作成してログイン
garmin_client = Garmin(email, password)
garmin_client.login()

print("###################################################dir(garmin_client)###################################################")
print(dir(garmin_client))
print("######################################################################################################")

# 指定した日付から今日までの期間を設定
#start_date = datetime.strptime("2023-01-01", "%Y-%m-%d")  # ここに開始日を設定
start_date = datetime.strptime("2023-11-30", "%Y-%m-%d")  # ここに開始日を設定
start_date = start_date.replace(hour=0, minute=0, second=0, microsecond=0)

end_date = datetime.today()

current_date = start_date
heart_rates = []

while current_date <= end_date:
    # 日付ごとの心拍数を取得
    heart_rate_data = garmin_client.get_heart_rates(current_date.strftime("%Y-%m-%d"))
    heart_rates.append(heart_rate_data)
    
    # 日付を1日進める
    current_date += timedelta(days=1)

# 結果を表示
for hr_data in heart_rates:
    print(hr_data)