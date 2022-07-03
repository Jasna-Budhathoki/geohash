from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

students = [{"Name":"Jasna"}]


@app.route("/jasna")
def me():
    return jsonify(students)





if __name__ == "__main__":
    app.run(host='localhost',port=7000,debug=True)
