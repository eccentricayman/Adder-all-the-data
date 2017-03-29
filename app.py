from flask import Flask, render_template, redirect, url_for
from utils import drugs, school_scores

app = Flask(__name__)

@app.route("/")
def home():
    return render_template( 'home.html' )


@app.route("/drugs/")
def drugs():
    pass

@app.route("/schoolScores/")
def school():
    pass


if __name__ == "__main__":
    app.debug == True
    app.run()
