# import necessary libraries
#from models import create_classes
import os
import math
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
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
loaded_model = joblib.load("decision_tree.sav")

#load scaler
scaler = joblib.load("Scaler.sav")

def convertvaluetonumeric(value):
    if value:
        return 1 
    else:
        return 0


# create route that renders index.html template
@app.route("/")
def home():
    return render_template("index_tree.html")

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
        budget_classes_budget_high = convertvaluetonumeric(request.form.getlist("high"))
        budget_classes_budget_low = convertvaluetonumeric(request.form.getlist("low"))
        budget_classes_budget_med = convertvaluetonumeric(request.form.getlist("med"))
        

        inputvalue = [[Action, Adventure, Animation, Biography, Comedy, Crime, Drama, Family, Fantasy, Horror, Mystery, Romance,
 SciFi,
 Thriller,
 lang_English,
 lang_French,
 lang_Japanese,
 lang_Korean,
 lang_Mandarin,
 lang_Spanish, 
 budget_classes_budget_high,
 budget_classes_budget_low,
 budget_classes_budget_med]]

        print(loaded_model.predict(inputvalue))

        return render_template("index_tree.html", data=loaded_model.predict(inputvalue))

    


if __name__ == "__main__":
     app.run(debug=True)
