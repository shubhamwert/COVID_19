import flask
import pandas as pd
import json
import utils.data_scarping as ds
app=flask.Flask(__name__)
with open('data/data.json) as f:
    data=json.load(f)
@app.route('/state_wise_data/',methods=['GET'])
def getData():
    return json.dumps(data)

@app.route('/update_data/',methods=['GET'])
def updateData():
    ds.updateData()
    return json.dumps({'response':True})
app.run(host='0.0.0.0',port=5000)
