from flask import Flask
from flask import request
import pandas as pd
import joblib
from flask_cors import CORS

model = joblib.load('best_model')
encoder = joblib.load('encoder')


app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def serve():
    return 'hello wrold'


@app.route('/predict', methods = ["POST"])
def prediction():
    data = request.json
    dict = {}
    dict['Year'] = data["Year"]
    dict['Month'] = data['Month']
    dict['Cost_Centre']	= data['Cost_Centre']
    dict['Account']	 = data['Account']
    dict['Account_Type'] = data['Account_Type']

    df = pd.DataFrame(dict, index = [0])
    X = encoder.transform(df)
    y_hat = model.predict(X)
    return str(y_hat[0])



if __name__=="__main__":
    app.run(host="0.0.0.0", threaded=True, port=5000)
