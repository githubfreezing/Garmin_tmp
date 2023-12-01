from datetime import date
import pandas as pd
from datetime import datetime, timezone, timedelta
from garminconnect import Garmin

# Garmin アカウント情報
email = "mtk.ms-590708@docomo.ne.jp"
password = "Basuke0829"

# Garmin に接続
connect = Garmin(email, password)
connect.login()

# 今日の日付
#昨日の日付
# 昨日の日付を取得
yesterday = date.today() - timedelta(days=1)
today = yesterday.strftime('%Y-%m-%d')
#today = date.today().strftime('%Y-%m-%d')

# 心拍数データの取得
heart_rates = connect.get_blood_pressure(today)

print("Blood Pressure Data:", heart_rates)

# # 日付と心拍数のリストを生成
# data = []
# for timestamp_ms, heart_rate in heart_rates["heartRateValues"]:
#     timestamp_s = timestamp_ms / 1000  # ミリ秒を秒に変換
#     date_time = datetime.fromtimestamp(timestamp_s, timezone.utc)  # UNIXタイムスタンプを日時に変換
#     formatted_date_time = date_time.strftime('%Y-%m-%d %H:%M')  # 日付と時間のフォーマット
#     data.append([formatted_date_time, heart_rate])

# # DataFrameを生成
# df = pd.DataFrame(data, columns=['日付', '心拍数'])

# # 結果を表示
# print(df)

# # DataFrameの最初の日付を取得（YYYY-MM-DD形式）
# file_date = df['日付'].iloc[0].split(' ')[0]

# # CSVファイル名を生成（例：get_heart_rates_2023-12-01.csv）
# csv_file_name = f"./get_heart_rates_{file_date}.csv"

# # CSVファイルに出力
# df.to_csv(csv_file_name, index=False)

# print(f"Data exported to {csv_file_name}")