import flask
import pandas as pd
import json
app=flask.Flask(__name__)
with open('data.json') as f:
    data=json.load(f)
@app.route('/state_wise_data/',methods=['GET'])
def getData():
    return json.dumps(data)

app.run()
