from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route("/get_state_names", methods=['GET'])
def get_state_names():
    response = jsonify({
        'states': util.get_state_names()
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/predict_home_price', methods=['GET','POST'])
def predict_home_price():
    living_space = float(request.form['Living_space'])
    state = request.form['State']
    rooms = request.form['Rooms']
    bathrooms = request.form['Bathrooms']
    resource = jsonify({
        'estimated_price': util.get_estimated_price(state,living_space,rooms,bathrooms)
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

if __name__ =="__main__":
    print("Server for home price prediction...")
    app.run()