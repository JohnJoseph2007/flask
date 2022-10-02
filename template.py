from flask import Flask

#CRUD (Create, Read, Update, Delete):
#Create => POST method
#Read => GET method
#Update => PUT method
#Delete => DEL method

#Data
eattoday = [
    {"name":"Donut", "time":"Before Lunch"},
    {"name":"Momos", "time":"Evening"}
]

#Creating Flask object
app = Flask(__name__)

#Default home message
@app.route("/")
def greet():
    return "Hi user, hope you have flask installed. I have been through way too much."

#Getting all the data
@app.route("/get", methods=["GET"])
def get():
    return jsonify({"data":eattoday})

#Getting any single point of data
@app.route("/getsingle/<int:index>", methods=["GET"])
def getsingle(index):
    return jsonify({"data":eattoday[index]})

#Posting or creating new data
@app.route("/post/<str:name>/<str:time>", methods=["POST"])
def post(name, time):
    newdish = {"name":name, "time":time}
    eattoday.append(newdish)
    return jsonify({"data":eattoday})

#Updating existing data
@app.route("/put/<int:index>/<str:name>", methods=["PUT"])
def put(index, name):
    eattoday[index]["name"] = name
    return jsonify({"data":eattoday})

#Deleting existing data (whole key, not a single field)
@app.route("/del/<int:index>", methods=["DEL"])
def delete(index):
    eattoday.pop(index)
    return jsonify({"data":eattoday})

if __name__ == "__main__":
    app.run(debug=True)