from flask import Flask, request, jsonify,render_template
import util

app = Flask(__name__)

@app.route('/')
def home():
    return "hi"





@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/predict_home_price', methods=['GET'])
def predict_home_price():
    try:
        total_sqft = float(request.args.get('total_sqft'))
        location = request.args.get('location')
        bhk = int(request.args.get('bhk'))
        bath = int(request.args.get('bath'))

        estimated_price = util.get_estimated_price(location, total_sqft, bhk, bath)

        response = jsonify({
            'estimated_price': round(estimated_price, 2)
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run(debug=True)
