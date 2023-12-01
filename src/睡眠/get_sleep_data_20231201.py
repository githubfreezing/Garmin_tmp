from datetime import date
import pandas as pd
from datetime import datetime, timezone
from garminconnect import Garmin
import csv

# Garmin アカウント情報
email = "mtk.ms-590708@docomo.ne.jp"
password = "Basuke0829"

# Garmin に接続
connect = Garmin(email, password)
connect.login()

# 今日の日付
today = date.today().strftime('%Y-%m-%d')

# 心拍数データの取得
sleep_data = connect.get_sleep_data(today)

# Function to convert GMT timestamp to local time and format it
def format_timestamp(timestamp):
    return datetime.fromtimestamp(timestamp/1000).strftime('%Y-%m-%d %H:%M:%S')

# Create and write to CSV
csv_filename = 'get_sleep_data_2023-11-30.csv'
with open(csv_filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Date', 'Time', 'Minute', 'Sleep'])

    # Write the sleep start and end times
    sleep_start = format_timestamp(sleep_data['dailySleepDTO']['sleepStartTimestampGMT'])
    sleep_end = format_timestamp(sleep_data['dailySleepDTO']['sleepEndTimestampGMT'])
    writer.writerow([sleep_start.split()[0], sleep_start.split()[1], sleep_start.split()[1].split(':')[1], 'Sleep Start'])
    writer.writerow([sleep_end.split()[0], sleep_end.split()[1], sleep_end.split()[1].split(':')[1], 'Sleep End'])

    # Write sleep movement data
    for movement in sleep_data['sleepMovement']:
        start = movement['startGMT']
        end = movement['endGMT']
        date, time = start.split('T')
        minute = time.split(':')[1]
        writer.writerow([date, time, minute, 'Sleep Movement'])
