from flask import Flask, render_template, request, json, Response,redirect,flash,url_for
from flask import Flask
import requests, json

kv=""

dburl="https://socialpancakes-d1dad.firebaseio.com/bdata/Users/.json"
key_url=(f"https://socialpancakes-d1dad.firebaseio.com/bdata/Users/{kv}.json")

app = Flask(__name__)

@app.route('/')
def hello_world():
   result = requests.get(dburl).json()
   resOut=[]
   for usr in result:
      user = result[usr]
      rec = {}
      rec['kv'] = usr
      rec["name"] = user["name"]
      rec['email'] = user['email']
      rec["comments"] = user["comments"]
      resOut.append(rec)
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
   result = requests.post(f"https://socialpancakes-d1dad.firebaseio.com/bdata/Users/.json",data=json.dumps(rec))
   return redirect("/")

@app.route('/delete/<kv>')
def deleteRec(kv):
   result = requests.delete(f"https://socialpancakes-d1dad.firebaseio.com/bdata/Users/{kv}.json")
   return redirect("/")

@app.route('/edit/<kv>')
def editRec(kv):
   result = requests.get(f"https://socialpancakes-d1dad.firebaseio.com/bdata/Users/{kv}.json").json()
   print(result)
   return render_template("edit.html", key=kv, user=result)

@app.route('/update', methods=['POST'])
def update_contact():
   toDelete = 'NOPE'
   key=request.form['key']
   name=request.form['name']
   email=request.form['email']
   comments=request.form['comments']
   try:
      toDelete = request.form['toDelete'] 
   except:
      print("Not deleted")
   if (toDelete == "deleteMe"):
      print(key)
      return redirect("/delete/"+key)
   else:
      rec = {}
      rec['key'] = key
      rec["name"] = name
      rec['email'] = email
      rec["comments"] = comments
      result = requests.put(f"https://socialpancakes-d1dad.firebaseio.com/bdata/Users/{key}.json",data=json.dumps(rec))
      print (result)
      return redirect("/")

"""

if __name__ == '__main__':
   app.run(debug=True, port=8000)

"""
