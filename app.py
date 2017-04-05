from flask import Flask, render_template, redirect, url_for, json, request
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

@app.route("/stateData/", methods=['GET','POST'])
def stateData():
    data = {}
    state = request.args.get('state')
    data['Drugs'] = interact.find_state_drugs(state)
    data['Scores'] = interact.find_state_scores(state)
    '''
    states = interact.get_state_codes()
    for name, state in states.items():
        if state != 'GA':
            data[state] = {}
            data[state]['Drugs'] = interact.find_state_drugs(state)
            data[state]['Scores'] = interact.find_state_scores(state)
    '''
    #print state
    return json.dumps( data )

if __name__ == "__main__":
    app.debug == True
    app.run()
