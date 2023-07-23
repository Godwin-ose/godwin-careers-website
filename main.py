from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS=[
  {
    'id':1,
    'title':'Data Analyst',
    'location':'Lagos, Nigeria',
    'Salary':'NGN 350,000'

  },

  {
    'id':2,
    'title':'Data Sciencist',
    'location':'Abuja, Nigeria',
    'Salary':'NGN 450,000'

  },

  {
    'id':3,
    'title':'Frontend Engineer',
    'location':'Port-Harcourt, Nigeria',
    'Salary':'NGN 250,000'

  },
  
  {
    'id':4,
    'title':'Backend Engineer',
    'location':'Remote',
    'Salary':'NGN 550,000'

  },
]

@app.route("/")
def hello_world():
  return render_template('home.html',
                         jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
  return jsonify (JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)