import pytz
from datetime import datetime

# Create a datetime object from the given timestamp
def dateconversion(date):
    timestamp = datetime.strptime(str(date), '%Y-%m-%d %H:%M:%S%z')

            # Convert the timezone from UTC to IST
    ist_timezone = pytz.timezone('Asia/Kolkata')
    ist_time = timestamp.astimezone(ist_timezone)

            # Format the IST time in a desired string format
    indian_timezone = ist_time.strftime('%Y-%m-%d %H:%M:%S%z')

            # Print the converted timestamp in IST
    return indian_timezone

# timestamp = datetime.strptime("2023-03-23 06:14:18+00:00", '%Y-%m-%d %H:%M:%S%z')

# # Convert the timezone from UTC to IST
# ist_timezone = pytz.timezone('Asia/Kolkata')
# ist_time = timestamp.astimezone(ist_timezone)

# # Format the IST time in a desired string format
# ist_time_str = ist_time.strftime('%Y-%m-%d %H:%M:%S%z')

# # Print the converted timestamp in IST
# print(ist_time_str)
