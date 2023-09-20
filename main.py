from flask import Flask


app = Flask(__name__)

@app.route("/")
def homepage():
    return "FakePinterest - Uma réplica do Pinterest!"


if __name__ == "__main__":
    app.run(debug=True)


