# import flask dependencies
from flask import Flask, request, make_response, jsonify

# initialize the flask app
app = Flask(__name__)

# default route
@app.route('/')
def index():
    return 'Hello World!'

# function for responses
def results():
    # build a request object
    req = request.get_json(force=True)

    # fetch action from json
    action = req.get('queryResult').get('action')

    # return a fulfillment response
    return {'fulfillmentText': 'succESS'}

# create a route for webhook
@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    # return response
    return make_response(jsonify(results()))

# run the app
if __name__ == '__main__':
      app.run(host='0.0.0.0', port=80)
"""
def model(text):
  import pandas as pd
  import numpy as np
  import matplotlib.pyplot as plt

  #importing Dataset
  dataset = pd.read_csv('Salary_Data.csv')
  X = dataset.iloc[:,:-1].values
  y = dataset.iloc[:,1].values

  #Spliting dataset into training set and train set
  from sklearn.model_selection import train_test_split
  X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=1/3,random_state=0)

  #Feature Scaling
  from sklearn.preprocessing import StandardScaler
  ss_X = StandardScaler()
  X_train = ss_X.fit_transform(X_train)
  x_test = ss_X.transform(X_test)￼
  ss_y = StandardScaler()
  y_train = ss_y.fit_transform(y_train)
  y_test = ss_y.transform(y_test)

  # Fitting Simple Linear Regression to Training set
  from sklearn.linear_model import LinearRegression
  reg = LinearRegression()
  reg.fit(X_train,y_train)

  #predicting values for test set
  y_pred = reg.predict(X_test)
"""

