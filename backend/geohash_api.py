import flask
from flask import request, jsonify, make_response
from geohash_decoder import decode
from geohash_encoder import encode
from flasgger import Swagger, swag_from
from baato import BaatoClient  #

app = flask.Flask(__name__)
app.config["DEBUG"] = True

client = BaatoClient(access_token="bpk.05j39KLSi-P80QvtSUdrMYpwuIqsgjTYlMuWtcvZ9UDZ")

template = {
    "swagger": "2.0",
    "info": {
        "title": "Geohash API",
        "description": "API for geohash encoder and decoder",
        "contact": {
            "reponsibleOrgnaization": "Kathmandu Living Labs",
            "responsibleDeveloper": "Jasna Budhathoki",
            "email": "jasna.budhathoki@kathmandulivinglabs.org",
        },
        "version": "0.0.1",
    },
    "basePath": "/api/v1/geohash",
    "schemes": ["http", "https"],
}

swagger = Swagger(app, template=template)


@app.route("/", methods=["GET"])
def home():
    return """<h1>Geohash Encoder/Decoder System</h1>
<p>A prototype API for converting geohash to latitude and longitude.</p>"""


# status code error 404


@app.errorhandler(404)  # handle 404 error - server cannot find the requested source
def handle_404_error(_error):
    return make_response(jsonify({"error": f"Not found"}), 404)


# status code error 400
@app.errorhandler(
    400
)  # server cannot or will not process the request due to a client error
def handle_400_error(_error):
    return make_response(jsonify({"error": "Bad Request"}), 400)


@app.route("/api/v1/geohash/decoder", methods=["GET"])
@swag_from("./docs/geohash.yml")
def api_geohash():
    if (
        "geohash" in request.args and request.args["geohash"].isalnum()
    ):  # Check if a geohash was provided as part of the URL.
        geohash_str = str(request.args["geohash"])
        decoded = decode(geohash_str)
    else:
        return jsonify(
            {"status": 400, "message": "Error: No correct geohash provided"}
        )  # handle 404 error - server cannot find the requested source

    results = []
    results.append(decoded)
    return jsonify(
        {"status": 200, "message": "success", "data": results}
    )  # If geohash is provided, display its long and lat.


@app.route("/api/v1/geohash/encoder", methods=["GET"])
@swag_from("./docs/encoder.yml")
def api_geohash_encoder():
    query_parameters = request.args
    geohash = ""

    latitude = query_parameters.get("latitude")
    longitude = query_parameters.get("longitude")
    if latitude == None or longitude == None:
        return {
            "status": 400,
            "message": "Either latitude or longitude data is missing",
        }

    if "latitude" in request.args and "longitude" in request.args:
        try:
            latitude = float(request.args["latitude"])
            longitude = float(request.args["longitude"])
            geohash = encode(latitude, longitude)
            response = client.reverse(lat=latitude, lon=longitude)  #
            data_1 = response["data"]  #
            status_1 = response["status"]  #
            return jsonify(
                {
                    "status": 200,
                    "message": "success",
                    "data": geohash,
                    "data_1": data_1,
                    "status_1": status_1,
                }
            )  #
        except:
            return jsonify(
                {
                    "status": 400,
                    "message": "Please provide latitude and longitude in the correct format",
                }
            )  # handle 404 error - server cannot find the requested source


if __name__ == "__main__":
    app.run(debug=True, port=8000)
