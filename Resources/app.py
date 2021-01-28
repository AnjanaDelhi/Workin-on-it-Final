# import necessary libraries
#from models import create_classes
import os
import math
import random
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
#import joblib
import pickle
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
filename = "decision_tree.sav"
#filename = "workin_model_liner.sav"
loaded_model = pickle.load(open(filename, 'rb'))

#load scaler
filename = "Scaler.sav"
scaler = pickle.load(open(filename, 'rb'))

#textgenerator
with open("generator/movie_titles.txt", "r") as file:
    allText = file.read() 
    words = list(map(str, allText.split())) 

actors = pd.read_csv('generator/actor_names.txt', header=None, names=['actor'])
genre = ['Action','Adventure','Animation','Biography','Comedy','Crime','Drama','Family','Fantasy','Horror','Mystery','Romance','Sci-Fi','Thriller']
language = ['English','French','Japanese','Korean','Mandarin','Spanish']



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

        value = loaded_model.predict(inputvalue)
        if value[0] == "income_low": 
            value_description = "Low Income (Less than $10,000,000)"
        elif value[0] == "income_med":
            value_description = "Medium Income (Between $10,000,000 to $60,000,000)"
        elif value[0] == "income_high":
            value_description =  "High Income (Above $60,000,000)"

        return render_template("index_tree.html", data=value_description)

        #print(loaded_model.predict(scaler.transform(inputvalue)))

        #return render_template("index_tree.html", data=10**loaded_model.predict(scaler.transform(inputvalue)))

@app.route("/get_quote")
def randomize():
    random1 = [actors.sample(n=1).values[0,0] + ' will be the lead actor in a(n) ' + random.choice(language) + ' ' + random.choice(genre) 
 + ' ' + 'titled ' + random.choice(words) + ' ' + random.choice(words)  + '.']
    return jsonify(random1)


if __name__ == "__main__":
     app.run(debug=True)
