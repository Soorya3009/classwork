# You are helping a travel blog store and manage recent trip details. Each trip includes a city name, the date it was visited (in the format dd-mm-yyyy), and a short comment. Your task is to:
# Create a Python module named tripdata.py with a function that returns trip details in dictionary format.
# In your main file, import the function and use it to build a list of trip dictionaries.
# For each trip:
#   Convert the date string into a date object.
#    Format the date to display as "Month Day, Year" (e.g., “May 15, 2023”).
# Convert the list of trip dictionaries to a JSON string and print it.

from datetime import datetime
import json

def get_trip(city, date_str, comment):
    return {
        "city": city,
        "date": date_str,
        "comment": comment
    }


trips = [
    get_trip("Delhi", "15-05-2023", "Amazing historical places"),
    get_trip("Goa", "10-12-2023", "Beautiful beaches"),
    get_trip("Jaipur", "20-01-2024", "Loved the forts and culture")
]

for trip in trips:
    date_obj = datetime.strptime(trip["date"], "%d-%m-%Y")
    trip["date"] = date_obj.strftime("%B %d, %Y")

json_data = json.dumps(trips, indent=4)

print(json_data)
