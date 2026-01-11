from flask import Flask, request, jsonify
from app.feature_engineering import hash_feature

app = Flask(__name__)


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    text = data.get("text", "")
    value = hash_feature(text)
    return jsonify({"prediction": value})


if __name__ == "__main__":
    print("Starting Flask app on 0.0.0.0:5000")
    app.run(host="0.0.0.0", port=5000, debug=False)
