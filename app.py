from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': "Cashier",
    'location': "Filinvest 1, Road, Batasan Hills, Quezon City",
    'salary': 'Php 600 per day',
    'work shift': "Day"
  },
  {
    'id': 2,
    'title': "Cook",
    'location': "Filinvest 1, Road, Batasan Hills, Quezon City",
    'salary': 'Php 700 per day',
    'work shift':  "Night"
  },
  {
    'id': 3,
    'title': "Inventory Manager",
    'location': "Filinvest 1 Road, Batasan Hills, Quezon City",
    'salary': 'Php 650 per day',
    'work shift': "Day"
  },
  {
    'id': 4,
    'title': "Admin",
    'location': "Visayas Street, Batasan Hills, Quezon City",
    'salary': 'Php 750 per day',
    'work shift':  "Day"
  }
]


@app.route("/") #so example facebook/jaymark ung jaymark ung route
def intro_header():
    return render_template('home.html', jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)