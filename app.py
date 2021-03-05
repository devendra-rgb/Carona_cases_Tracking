from flask import Flask,render_template
import pygal
import json

app=Flask(__name__)
ma=pygal.maps.world.World()
ma.title='Carona cases On 14/12/2020'
with open('cleaned_data.json') as f:
    dictionary=json.load(f)
ma.add('Cases',dictionary)
ma=ma.render_data_uri()



@app.route('/')
def line_route():
  
  return render_template('charts.html',chart=ma)

if __name__=='__main__':
    app.run()
