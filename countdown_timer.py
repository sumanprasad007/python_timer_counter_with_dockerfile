# import time

# def countdown(time_sec):
#     while time_sec:
#         mins, secs = divmod(time_sec, 60)
#         timeformat = '{:02d}:{:02d}'.format(mins, secs)
#         print(timeformat, end='\r')
#         time.sleep(1)
#         time_sec -= 1
        
#         print("stop")
# #num=int(input("Set your timer in seconds: ")) 
# num=(20) # can use static value of count down as input is not possible to give while running as docker container

# countdown(num)
#----------------------Solution to error of input [Using environment variable & defined counter value as 60 but you can change it as per your need]-----------------------

import time
import os

def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        time_sec -= 1

    print("stop")

num = int(os.environ.get("TIMER_SECONDS", 60))
print("Counter is running for")
countdown(num)


