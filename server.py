from flask import Flask, jsonify
from flask_cors import CORS


 

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})
@app.route("/api/news")
def get_news():
    news = [
    {
        "name": "Доброе утро",
        "description": "Счастья всем",
        "date": "2025-03-26",
    },
    {
        "name": "Доброе утро",
        "description": "Счастья всем",
        "date": "2025-03-26",
    },
    {
        "name": "Доброе утро",
        "description": "Счастья всем",
        "date": "2025-03-26",
    }
]
    return jsonify(news)

def main():
    app.run("0.0.0.0",8010, True)

if __name__ == "__main__":
    main()