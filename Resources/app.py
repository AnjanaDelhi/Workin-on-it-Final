# import necessary libraries
#from models import create_classes
import os
import math
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
import joblib
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#load model
loaded_model = joblib.load("workin_model_liner.sav")

#load scaler
scaler = joblib.load("Scaler.sav")

def convertvaluetonumeric(value):
    if value:
        return 1 
    else:
        return 0

#################################################
# Database Setup
#################################################
# from sqlalchemy.ext.automap import automap_base
# from sqlalchemy.orm import Session
# from sqlalchemy import create_engine, func
# from flask_sqlalchemy import SQLAlchemy
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '') or "sqlite:///wh20.sqlite"

# # Remove tracking modifications
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = create_engine("sqlite:///wh20.sqlite", connect_args={'check_same_thread': False})
# session = Session(bind=db)

# reflect an existing database into a new model
# Base = automap_base()
# # reflect the tables
# Base.prepare(db, reflect=True)

# # Save reference to the table
# Country = Base.classes.wh20

# create route that renders index.html template
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/genre")
def happy():
    return render_template("genre.html")

@app.route("/top10")
def life():
    return render_template("top10.html")


# Query the database and send the jsonified results
@app.route("/", methods=["GET", "POST"])
def send():
    if request.method == "POST":
        Action = convertvaluetonumeric(request.form.getlist("action"))
        Adventure = convertvaluetonumeric(request.form.getlist("adventure"))
        Animation = convertvaluetonumeric(request.form.getlist("animation"))
        Biography = convertvaluetonumeric(request.form.getlist("biography"))
        Comedy = convertvaluetonumeric(request.form.getlist("comdey"))
        Crime = convertvaluetonumeric(request.form.getlist("crime"))
        Drama = convertvaluetonumeric(request.form.getlist("drama"))
        Family = convertvaluetonumeric(request.form.getlist("family"))
        Fantasy = convertvaluetonumeric(request.form.getlist("fantasy"))
        Horror = convertvaluetonumeric(request.form.getlist("horror"))
        Mystery = convertvaluetonumeric(request.form.getlist("mystery"))
        Romance = convertvaluetonumeric(request.form.getlist("romance"))
        SciFi = convertvaluetonumeric(request.form.getlist("scifi"))
        Thriller = convertvaluetonumeric(request.form.getlist("thriller"))
        lang_English = convertvaluetonumeric(request.form.getlist("english"))
        lang_French = convertvaluetonumeric(request.form.getlist("french"))
        lang_Japanese = convertvaluetonumeric(request.form.getlist("japanese"))
        lang_Korean = convertvaluetonumeric(request.form.getlist("korean"))
        lang_Mandarin = convertvaluetonumeric(request.form.getlist("mandarin"))
        lang_Spanish = convertvaluetonumeric(request.form.getlist("spanish"))
        log_budget = math.log(int(request.form.getlist("budget")[0]))
        

        inputvalue = [[Action, Adventure, Animation, Biography, Comedy, Crime, Drama, Family, Fantasy, Horror, Mystery, Romance,
 SciFi,
 Thriller,
 log_budget,
 lang_English,
 lang_French,
 lang_Japanese,
 lang_Korean,
 lang_Mandarin,
 lang_Spanish]]

        print(loaded_model.predict(scaler.transform(inputvalue)))

        return render_template("index.html", data=10**loaded_model.predict(scaler.transform(inputvalue)))

    


if __name__ == "__main__":
     app.run(debug=True)
