import flask
import pandas as pd
import json
import utils.data_scarping as ds
import pygal 
import analysis as an
app=flask.Flask(__name__)
with open('data/data.json') as f:
    data=json.load(f)
@app.route('/state_wise_data/',methods=['GET'])
def getData():
    return json.dumps(data)

@app.route('/update_data/',methods=['GET'])
def updateData():
    ds.updateData()
    return json.dumps({'response':True})

@app.route('/svg_state_wise_data',methods=['GET'])
def svg_state_data():
    a=an.createSvgStateWise()
    return a.render_response()
@app.route('/',methods=['GET'])
def index():
    a=an.createSvgStateWise(12)
    return flask.render_template('index.html',graph_data=a.render(),table_data=a.render_table())

app.run(host='0.0.0.0',port=5000)
