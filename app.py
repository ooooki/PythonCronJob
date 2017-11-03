import requests
import json
import pytz
from pytz import timezone
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

#@sched.scheduled_job('interval', minutes=1)
#def timed_job():
#    print('This job is run every three minutes.')

@sched.scheduled_job('cron', day_of_week='mon,tue,wed,thu,fri,sat,sun', hour=0,timezone ='Asia/Kolkata')
def scheduled_job():
    print('This job is run every weekday at midnight.')
    result = bookApt()


def bookApt():
    south_africa = timezone('Asia/Kolkata')
    sa_time = datetime.now(south_africa)
    date_para = sa_time.strftime('%Y-%m-%d')
    print(date_para)


    url = 'your url'

    data = {"name":"morpheus","job":"zion resident"}


    #data_len = len(data)
    #print(data_len)

    put_headers = {
  "Content-Type":"application/json"
}


    print(data)

    #response = requests.put(url, data=data,headers=headers)
    response = requests.put(url, data=json.dumps(data,separators=(', ', ': ')),headers=put_headers)

    #jsonDict = json.loads(response.text)
    #print(jsonDict)
    responseString = response.text

    print(responseString)

    return responseString

sched.start()