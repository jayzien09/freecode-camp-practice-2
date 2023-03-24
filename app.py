from flask import Flask, render_template, jsonify
from database import load_jobs_from_db, load_job_from_db

app = Flask(__name__)


@app.route("/") #so example facebook/jaymark ung jaymark ung route
def intro_header():
  jobs = load_jobs_from_db()
  return render_template('home.html', jobs=jobs)

@app.route("/api/jobs")
def list_jobs():
  jobs = load_jobs_from_db()
  return jsonify(jobs)

@app.route("/job/<id>")
def show_job(id):
  job_description = load_job_from_db(id)
  return jsonify(job_description)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)