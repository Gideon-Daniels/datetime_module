from datetime import datetime, timedelta

current_date = datetime.today()  # gets today date
# displays ten dates
print(current_date.strftime("%Y-%m-%d"))
for x in range(1, 10):
    added_date = current_date + timedelta(days=14)  # timedelta adds days
    current_date = added_date
    print(added_date.strftime("%Y-%m-%d"))
# get datetime 2 days in past

