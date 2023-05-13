h, m = map(int, input().split())
flight_duration = 108
return_time = (h * 60 + m + flight_duration) % (24 * 60)
return_h = return_time // 60
return_m = return_time % 60
print(return_h, return_m)