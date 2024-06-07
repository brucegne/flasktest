from flask import Flask, render_template, request, json, Response,redirect,flash,url_for
from flask_bootstrap import Bootstrap5
import pyrebase


firebaseConfig = {
  "apiKey": "AIzaSyAK2XApgMbt7DE8tXiIdn9pPMUNvZS5tCA",
  "authDomain": "socialpancakes-d1dad.firebaseapp.com",
  "databaseURL": "https://socialpancakes-d1dad.firebaseio.com",
  "projectId": "socialpancakes-d1dad",
  "storageBucket": "socialpancakes-d1dad.appspot.com",
  "messagingSenderId": "812779768104",
  "appId": "1:812779768104:web:0e83d4f73e65f1061e681d"
}

firebase = pyrebase.initialize_app(firebaseConfig)

auth = firebase.auth()
db = firebase.database()
storeage = firebase.storage()

app = Flask(__name__)

@app.route('/')
def hello_world():
   result = db.child('bdata').child('Users').get()
   resOut=[]
   for user in result.each():
      rec = {}
      rec['kv'] = user.key()
      rec["name"] = user.val()["name"]
      rec['email'] = user.val()['email']
      rec["comments"] = user.val()["comments"]
      resOut.append(rec)
#   return (resOut)
   return render_template("index.html", users=resOut)

@app.route('/new')
def addNew():
   return render_template("new.html")

@app.route("/add", methods=["POST"])
def NewCont():
   name=request.form['name']
   email=request.form['email']
   comments=request.form['comments']
   rec = {}
   rec["name"] = name
   rec['email'] = email
   rec["comments"] = comments
   result = db.child('bdata').child('Users').push(rec)
   return redirect("/")

@app.route('/delete/<kv>')
def deleteRec(kv):
   result = db.child('bdata').child('Users').child(kv).remove()
   return redirect("/")


@app.route('/edit/<kv>')
def editRec(kv):
   result = db.child('bdata').child('Users').child(kv).get()
   print(result.val())
   return render_template("edit.html", key=result.key(), user=result.val())

@app.route('/update', methods=['POST'])
def update_contact():
   key=request.form['key']
   name=request.form['name']
   email=request.form['email']
   comments=request.form['comments']
   rec = {}
   rec['key'] = key
   rec["name"] = name
   rec['email'] = email
   rec["comments"] = comments
   result = db.child('bdata').child('Users').child(key).update(rec)

   print(key, name, comments)
   return redirect("/")
