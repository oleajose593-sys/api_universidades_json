from flask import Flask, Response
import json

app = Flask(__name__)

@app.route("/")
def ver_json():

    with open("universidades.json", encoding="utf-8") as f:

        data = json.load(f)

    return Response(

        json.dumps(data, indent=4, ensure_ascii=False),

        mimetype="application/json"
    )

if __name__ == "__main__":

    app.run(port=5001)