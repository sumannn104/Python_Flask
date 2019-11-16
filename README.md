# Deploy_Machine_Learning_model_in_Flask
Deploying  a machine learning model in Python using Flask

**This project is based on "Build a flask app to server a machine learning model as a RESTful web service" by a-djebali.**

We have a lot of tutorials for building machine learning models and testing their accuracy metrics and playing aroung with the parameters to improve the metrics.But ultimately, in order to show the results to other people we need to deploy thr model as web solution or an application.
For those working mainly in machine learning and python, FLASK (a micro web framework written in Python) will be easy to work with.

This project si organized as follows:

1. A model to predict the type of iris Plant, based on  the famous IRIS dataset.It depends on four parameters, given in the jupyter notebook given
2. Save the model using pickle
3. We have app.py which where the flask application is written
4.The saved model is used in the app.py, to serve the requests
To check a demo:

1. Clone this repo
2.Run the flask app by ( $python app.py) in a virtual environment with most ofthe major libraries
   You may use a virtual environment in Anaconda. 
