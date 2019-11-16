import numpy as np
from flask import Flask, abort, jsonify, request,render_template
import cloudpickle as pickle 

random_forest_model = pickle.load(open("rfc.pkl","rb"))

app = Flask(__name__)

@app.route('/')
def render_static():
     print("yes")
     
     return render_template('%s.html' %"index")
    
@app.route('/predict_api', methods=['POST'])
def predict():
    p1=request.form.get('p1')
    p2=request.form.get('p2')
    p3=request.form.get('p3')
    p4=request.form.get('p4')
    # Convert JSON to numpy array
    predict_request = [p1,p2,p3,p4 ]# [data['sl'],data['sw'],data['pl'],data['pw']]
    predict_request = np.reshape(np.array(predict_request),(1,len(predict_request)))

     # Predict using the random forest model
    y = random_forest_model.predict(predict_request)

     # Return predictio
    output = y[0]
    
    r=results=int(output)
     # Error checking
     #data = request.get_json(force=True)
     
    return render_template('%s.html' % "results",r=r)

if __name__ == '__main__':
     app.run(port = 9000, debug = True)
