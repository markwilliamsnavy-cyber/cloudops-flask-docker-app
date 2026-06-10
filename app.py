from flask import Flask, jsonify
from datetime import datetime, timezone
import os

app = Flask(__name__)

APP_NAME = os.getenv("APP_NAME", "CloudOps Flask App")
ENVIRONMENT = os.getenv("ENVIRONMENT", "local")


@app.route("/")
def home():
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>{APP_NAME}</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 40px;
                background-color: #f4f6f8;
                color: #222;
            }}
            .card {{
                background: white;
                padding: 30px;
                border-radius: 10px;
                max-width: 700px;
                box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            }}
            h1 {{
                color: #1f2937;
            }}
            code {{
                background: #eef2f7;
                padding: 3px 6px;
                border-radius: 4px;
            }}
        </style>
    </head>
    <body>
        <div class="card">
            <h1>{APP_NAME}</h1>
            <p>This is a Python Flask application running locally.</p>
            <p>Project goal: containerize this app with Docker and deploy it on AWS EC2.</p>
            <p><strong>Environment:</strong> {ENVIRONMENT}</p>

            <h3>Available endpoints:</h3>
            <ul>
                <li><code>/</code> - Home page</li>
                <li><code>/health</code> - Health check</li>
                <li><code>/status</code> - Application status</li>
            </ul>
        </div>
    </body>
    </html>
    """


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "service": APP_NAME,
        "environment": ENVIRONMENT
    }), 200


@app.route("/status")
def status():
    return jsonify({
        "service": APP_NAME,
        "environment": ENVIRONMENT,
        "message": "Application is running successfully",
        "timestamp": datetime.now(timezone.utc).isoformat()
    }), 200


if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
