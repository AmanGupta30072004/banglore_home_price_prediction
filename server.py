from flask import Flask, request, jsonify, render_template
import util

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/predict_home_price', methods=['GET','POST'])
def predict_home_price():
    if request.method=='GET':
        return render_template('home.html')
    else:
        total_sqft = float(request.form.get('uiSqft', 0))
        location = request.form.get('uiLocations', '')
        bhk = int(request.form.get('uiBHK', 0))
        bath = int(request.form.get('uiBathrooms', 0))

        estimated_price = util.get_estimated_price(location, total_sqft, bhk, bath)
    
        response = jsonify({'estimated_price': estimated_price})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
   

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run(port=5001, debug=True)

