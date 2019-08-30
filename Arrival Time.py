from datetime import datetime,timedelta

departure = datetime.now()

distance=5
speed=10

time = distance/speed

arrival = departure + timedelta(hours=time)

print(f"The boat Departure time: {departure.time()}")
print(f"The boat will Arrive at {arrival.time()}")