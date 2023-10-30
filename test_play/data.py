import datetime

appointedTime="2023-04-18"
appointed_time=datetime.datetime.strptime(appointedTime,"%Y-%m-%d")

curr_datetime=datetime.datetime.now()
minus_date=curr_datetime-appointed_time
print(minus_date.days)