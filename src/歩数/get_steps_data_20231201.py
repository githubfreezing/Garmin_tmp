from datetime import date
import pandas as pd
from datetime import datetime, timezone
from garminconnect import Garmin

# Garmin アカウント情報
email = "mtk.ms-590708@docomo.ne.jp"
password = "Basuke0829"

# Garmin に接続
connect = Garmin(email, password)
connect.login()

# 今日の日付
today = date.today().strftime('%Y-%m-%d')

# 歩数データの取得
step_data = connect.get_steps_data(today)

# 日付と歩数のリストを生成
data = []
for entry in step_data:
    # GMT時刻をローカル時刻に変換（必要に応じて）
    date_time = datetime.strptime(entry['startGMT'], '%Y-%m-%dT%H:%M:%S.%f')
    formatted_date_time = date_time.strftime('%Y-%m-%d %H:%M')
    
    # リストに追加
    data.append([formatted_date_time, entry['steps']])

# DataFrameを生成
df = pd.DataFrame(data, columns=['日付', '歩数'])

# 結果を表示
print(df)

# DataFrameの最初の日付を取得（YYYY-MM-DD形式）
file_date = df['日付'].iloc[0].split(' ')[0]

# CSVファイル名を生成（例：get_heart_rates_2023-12-01.csv）
csv_file_name = f"./get_steps_data_{file_date}.csv"

# CSVファイルに出力
df.to_csv(csv_file_name, index=False)

print(f"Data exported to {csv_file_name}")