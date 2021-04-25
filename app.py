from flask import Flask,render_template
import pygal
import json
import requests
from apscheduler.schedulers.background import BackgroundScheduler
import time

app=Flask(__name__)
def refresh():
    url='https://covid.ourworldindata.org/data/owid-covid-data.json'
    a=requests.get(url)
    c=a.json()
    countries=[]
    for i in c.keys():
        countries.append(i)
        data={}
    for i in countries:
        try:
            cases=c[i]['data'][-1]['total_cases']
            j=i.lower()[:2]
            if j in data:
                data[j]=cases
            else:
                data[j]=cases
        except KeyError:
            continue
    date=c[i]['data'][-1]['date']
    a=pygal.maps.world.World()
    a.add('Cases',data)
    a.title="COVID-19 Cases Up to the date "+date
    a=a.render_data_uri()
    return a




@app.route('/')
def line_route():
  
  return render_template('charts.html',chart=refresh())

if __name__=='__main__':
  app.run()
