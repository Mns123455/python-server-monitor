from flask import Flask, jsonify
import os
import time

app = Flask(__name__)
start_time = time.time()

@app.route("/")
def home():
    return jsonify(
        application="Python Server Monitor",
        version="1.0",
        status="running"
    )

@app.route("/health")
def health():
    return jsonify(status="UP")

@app.route("/uptime")
def uptime():
    seconds = int(time.time() - start_time)
    return jsonify(uptime_seconds=seconds)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
