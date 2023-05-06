import time
import os

def countdown(time_sec):
    for t in range(time_sec, 0, -1):
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)

    print("stop")

num = int(os.environ.get("TIMER_SECONDS", 5))
print("Counter is running for:", num, "seconds⏰")
countdown(num)
print("Successfully, run the timer🎉")
