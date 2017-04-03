from flask import Flask, render_template, redirect, url_for, json
from utils import drugs, school_scores, interact

app = Flask(__name__)

@app.route("/")
def home():
    return render_template( 'home.html' )

@app.route("/corrs/", methods=['POST'])
def corrs():
    return json.dumps(interact.state_corrs(2014))

@app.route("/nationalData/", methods=['GET'])
def nationalData():
    data = { }
    data['Drugs'] = find_national_drugs()
    data['Scores'] = find_national_scores()
    return json.dumps( data ) 

if __name__ == "__main__":
    app.debug == True
    app.run()
