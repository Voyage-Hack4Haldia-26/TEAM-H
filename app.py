import os
from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

app = Flask(__name__)
CORS(app)
BASE = os.path.dirname(os.path.abspath(__file__))


@app.get("/")
def index():
    return send_from_directory(BASE, "index.html")


@app.get("/health")
def health():
    return jsonify(status="ok", project="Team H: Live Canteen Order Tracker", stack="flask")

@app.route("/api/orders", methods=["POST"])
def ep_0(**kwargs):
    # TODO: Place an order
    return jsonify(error="Not implemented", todo="Place an order"), 501

@app.route("/api/orders/<id>", methods=["PATCH"])
def ep_1(**kwargs):
    # TODO: Move to the next status
    return jsonify(error="Not implemented", todo="Move to the next status"), 501

@app.route("/api/orders/stream", methods=["GET"])
def ep_2(**kwargs):
    # TODO: SSE stream of order updates
    return jsonify(error="Not implemented", todo="SSE stream of order updates"), 501


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)
