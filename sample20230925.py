import datetime
from garminconnect import (
    Garmin
)

def init_api():
    api = Garmin('s.katsumata1988@gmail.com', 'Lemoned622')
    #api = Garmin('mtk.ms-590708@docomone.jp', 'Basuke0829')
    api.login()

    return api

api = init_api()

start_date = datetime.date(2023, 9, 24)
end_date = datetime.date(2023, 9, 26)

activities = api.get_activities_by_date(
                start_date.isoformat(), end_date.isoformat(), 'cycling')

print("activities")
print(activities)

for activity in activities:
    activity_id = activity["activityId"]
    gpx_data = api.download_activity(
                        activity_id, dl_fmt=api.ActivityDownloadFormat.GPX
                    )

    output_file = f"./cycle_trips_kml/{str(activity_id)}.KML"
    with open(output_file, "wb") as fb:
        fb.write(gpx_data)

print("Finished....")