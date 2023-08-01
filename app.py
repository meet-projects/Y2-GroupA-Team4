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


@app.route('/', methods=['GET', 'POST'])
def zakat():
    money = ''
    zakat = ''
    if request.method == 'POST':
        try:
            money = request.form['zakat']
            x = round(float(money)*0.025,2)
            zakat = { 'zakat': x }
            db.child("zakat").set(zakat)            
            db.child("zakat").update(zakat)
            zakat = db.child("zakat").get().val()
            zakat = zakat['zakat']
        except Exception as e:
            print(e)
            zakat = 'Error'
        return render_template('index.html', zakat = zakat)
    return render_template('index.html', zakat = zakat)




#Code goes above here

if __name__ == '__main__':
    app.run(debug=True)
