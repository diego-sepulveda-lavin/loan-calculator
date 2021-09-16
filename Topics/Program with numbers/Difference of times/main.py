# put your python code here
walk_hour = int(input())
walk_minute = int(input())
walk_second = int(input())

rain_hour = int(input())
rain_minute = int(input())
rain_second = int(input())

seconds_in_hour = 3600
seconds_in_minute = 60

hours_elapsed = rain_hour - walk_hour
minutes_elapsed = rain_minute - walk_minute
seconds_elapsed = rain_second - walk_second

total_time_elapsed_in_secs = (hours_elapsed * seconds_in_hour) + (minutes_elapsed * seconds_in_minute) + seconds_elapsed
print(total_time_elapsed_in_secs)
