from flask import Flask, url_for, request, render_template, jsonify
from apscheduler.schedulers.background import BackgroundScheduler
from Datamanagement import Datamanagement

ARCEUS = Datamanagement()
sched = BackgroundScheduler()
sched.add_job(ARCEUS.get_all_data, 'interval', minutes = 1)
sched.start()
ARCEUS.get_all_data()

app = Flask(__name__)

@app.route("/")
def index():
    return(render_template('ortswahl.html'))
    
@app.route("/pokemon", methods=['GET', 'POST'])
def pokemon():
    return(jsonify(ARCEUS.pokemon))

@app.route("/pokestops", methods=['GET', 'POST'])
def pokestops():
    return(jsonify(ARCEUS.pokestops)) 

@app.route("/quests", methods=['GET', 'POST'])
def quests():
    return(jsonify(ARCEUS.quests))  

@app.route("/raids", methods=['GET', 'POST'])
def raids():
    return(jsonify(ARCEUS.raids))

@app.route("/gyms", methods=['GET', 'POST'])
def gyms():
    return(jsonify(ARCEUS.gyms))

@app.route("/gymdetails", methods=['GET', 'POST'])
def gymdetails():
    return(jsonify(ARCEUS.gymdetails))


if __name__ == '__main__':
    app.run(port=5000, debug=True, host="0.0.0.0")