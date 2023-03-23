from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': "Cashier",
    'location': "Filinvest 1, Road",
    'salary': 'Php 600 per day'
  },
  {
    'id': 2,
    'title': "Cook",
    'location': "Filinvest 1, Road",
    'salary': 'Php 700 per day'
  },
  {
    'id': 3,
    'title': "Inventory Manager",
    'location': "Filinvest 1, Road",
    'salary': 'Php 650 per day'
  },
  {
    'id': 4,
    'title': "Admin",
    'location': "Filinvest 1, Road",
    'salary': 'Php 750 per day'
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