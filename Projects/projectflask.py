from flask import Flask
from flask import jsonify

app = Flask(__name__)

contacts = [
    {"number":"67250763248", "name":"Armani Daniels"},
    {"number":"59373758696", "name":"Magdalena Newton"},
    {"number":"52683370564", "name":"Nicholas Butler"},
    {"number":"03511597667", "name":"Landyn Meadows"},
    {"number":"94693706145", "name":"Gracie Rich"},
    {"number":"89430164419", "name":"Molly Bishop"},
    {"number":"12674844284", "name":"Beau Andersen"},
    {"number":"33899247909", "name":"Pranav Spence"},
    {"number":"65120534745", "name":"Lee Griffin"},
    {"number":"04216256538", "name":"Kaylin Bernard"}
]

@app.route("/greet=<string:name>")
def greeting(name):
    return f"Hi, {name}"

@app.route("/add-data&n=<int:num>&na=<string:name>", methods=["POST"])
def add_task(num, name):
    newcontact = {"number":num, "name":name}
    contacts.append(newcontact)
    return jsonify({"data":contacts})

@app.route("/get-data", methods=["GET"])
def get_data():
    return jsonify({"data":contacts})

@app.route("/get-single&<int:index>", methods=["GET"])
def get_single(index):
    return jsonify({"data":contacts[index]})

@app.route("/update&i=<int:index>&n=<int:num>", methods=["PUT"])
def update(index, num):
    contacts[index]["number"] = num
    return jsonify({"data":contacts})

@app.route("/del&i=<int:index>", methods=["DELETE"])
def delete(index):
    contacts.pop(index)
    return jsonify({"data":contacts})

if __name__ == "__main__":
    app.run(debug=True, port=3000)

