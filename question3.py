import requests
import datetime as dt
import os
#from dotenv import load_dotenv, find_dotenv    #testing from virtual environment

#load_dotenv(find_dotenv())                     #testing from virtual environment

website = os.getenv('site')
iterate = int(os.getenv('times'))

totalTime = dt.timedelta(0, 0, 0)

for i in range(0,iterate):
    x = requests.get(website)
    #print(x.elapsed)                       #testing
    totalTime += x.elapsed

print('Website url: ' + website + '\nNumber of Hits: ' + str(iterate) + '\n\nDays: ' + str(totalTime.days) + '\nSeconds: ' + str(totalTime.seconds) + '\nMicroseconds: ' + str(totalTime.microseconds))
