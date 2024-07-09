from flask import Flask



app = Flask(__name__)

@app.route("/app")
def retApp():
    return "Hello"


if __name__ in "__main__":
    app.run(debug=True)

from controller import *