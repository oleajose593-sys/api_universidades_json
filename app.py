from flask import Flask, Response, request
import json

app = Flask(__name__)

# 🔹 VER JSON
@app.route("/")
def ver_json():

    with open("universidades.json", encoding="utf-8") as f:
        data = json.load(f)

    return Response(
        json.dumps(data, indent=4, ensure_ascii=False),
        mimetype="application/json"
    )


# 🔥 RECIBIR JSON DESDE TU ADMIN
@app.route("/universidades", methods=["POST"])
def actualizar_json():

    nuevas_universidades = request.json

    with open("universidades.json", "w", encoding="utf-8") as f:
        json.dump(nuevas_universidades, f, indent=4, ensure_ascii=False)

    return {"mensaje": "JSON actualizado correctamente"}, 200


if __name__ == "__main__":
    app.run(port=5001)