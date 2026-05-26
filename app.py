from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def running():
    return "Job Application Assistant API is running"

@app.route("/jobs")
def jobs():
    job_list = [
        {"title": "Data Scientist", "company": "IBM"},
        {"title": "ML Engineer", "company": "Google"},
        {"title": "CyberSecurity Engineer", "company": "Flare"}
    ]
    return jsonify(job_list)
        

if __name__ == "__main__":
    app.run(debug=True)