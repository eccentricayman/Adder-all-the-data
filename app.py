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
    data['Drugs'] = interact.find_national_drugs()
    data['Scores'] = interact.find_national_scores()
    #print json.dumps( data)
    return json.dumps( data )

@app.route("/stateData/", methods=['GET'])
def stateData(state):
    data = {}
    data['Drugs'] = interact.find_state_drugs(state)
    data['Scores'] = interact.find_state_scores(state)
    return [json.dumps( data ), states, state]

if __name__ == "__main__":
    app.debug == True
    app.run()
