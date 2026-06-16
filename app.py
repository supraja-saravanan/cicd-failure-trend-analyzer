from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>🚀 CI/CD Demo Application</h1>
    <p>Status: Running</p>
    <p>Version: 1.0.0</p>
    """

@app.route("/api/status")
def api_status():
    return jsonify({
        "app": "CI/CD Failure Trend Analyzer Demo",
        "status": "healthy",
        "version": "1.0.0"
    })

@app.route("/fail")
def fail():
    raise Exception("Forced failure for demo")

if __name__ == "__main__":
    app.run()
