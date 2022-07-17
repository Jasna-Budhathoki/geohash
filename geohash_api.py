import flask
from flask import request, jsonify, make_response
from geohash_decoder import decode
from geohash_encoder import encode

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Geohash Encoder/Decoder System</h1>
<p>A prototype API for converting geohash to latitude and longitude.</p>'''

# status code error 404

@app.errorhandler(404) #handle 404 error - server cannot find the requested source 
def handle_404_error(_error):
    return make_response(jsonify({'error': f'Not found'}), 404)


# status code error 400
@app.errorhandler(400) #server cannot or will not process the request due to a client error
def handle_400_error(_error):
    return make_response(jsonify({'error': 'Bad Request'}), 400)


@app.route('/api/v1/geohash', methods=['GET'])
def api_geohash():
    # Check if a geohash was provided as part of the URL.
    # If geohash is provided, display its long and lat.
    # If an incorrect geohash is provided, return an error.
    if 'geohash' in request.args and request.args['geohash'].isalnum():
        geohash_str = str(request.args['geohash'])
        decoded = decode(geohash_str)
    else:
        return jsonify({"status": 400, "message": "Error: No correct geohash provided"})  #handle 404 error - server cannot find the requested source 


    results = []
    results.append(decoded)
    return jsonify({"status": 200, "message": "success", "data": results})


@app.route('/api/v1/geohash/encoder', methods=['GET'])
def api_geohash_encoder():
    query_parameters = request.args
    geohash = ""
    
    latitude = query_parameters.get('latitude')
    longitude = query_parameters.get('longitude')
    if latitude == None or longitude == None:
        return({"status": 400, "message": "Either latitude or longitude data is missing"})

    if 'latitude' in request.args and 'longitude' in request.args:
        try:
            latitude = float(request.args['latitude'])
            longitude = float(request.args['longitude'])
            geohash = encode(latitude, longitude)
            return jsonify({"status": 200, "message": "success", "data": geohash})
        except:
            return jsonify({"status": 400, "message": "Please provide latitude and longitude in the correct format"})  #handle 404 error - server cannot find the requested source 

if __name__ == "__main__":
    app.run(debug=True, port=9000)
