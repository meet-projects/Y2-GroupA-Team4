from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'

config = {
    "apiKey": "AIzaSyC05n1tnpMMBpMna5SVTDH9deLVA9zIrss",
    "authDomain": "travlerpack-ec5ab.firebaseapp.com",
    "databaseURL": "https://travlerpack-ec5ab-default-rtdb.firebaseio.com",
    "projectId": "travlerpack-ec5ab",
    "storageBucket": "travlerpack-ec5ab.appspot.com",
    "messagingSenderId": "1017759641",
    "appId": "1:1017759641:web:fc578430845db10e3c3508",
    "measurementId": "G-B2YPMZ3MKN",
}

fb = pyrebase.initialize_app(config)
auth = fb.auth()
db = fb.database()

#Code goes below here

@app.route("/", methods=["GET", "POST"])
def root():
    if request.method == "POST":
        try:
            organization = request.form["org"]
            email = request.form["email"]
            phone = request.form["phone"]
            donation = request.form["donations"]

            dictionary = {
                "email"   : email,
                "phone"   : phone,
                "donation": donation
            }

            if db.child(organization) != None:
                db.child(organization).update(dictionary)
            else:
                db.child(organization).set(dictionary)
        except:
            pass

#Code goes above here

if __name__ == '__main__':
    app.run(debug=True)
