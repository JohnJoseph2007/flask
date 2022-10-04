from flask import Flask, jsonify, request
from classify import poor

app = Flask(__name__)

@app.route("/image", methods=["POST"])
def image():
    img = request.files.get("hahakey")
    ugh = poor(img)
    return jsonify({"data":ugh})

if __name__ == "__main__":
    app.run(debug=True, port=3000)