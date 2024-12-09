from flask import Flask
from flask import request, render_template
import textblob
import google.generativeai as genai
import os

app = Flask(__name__)
api = os.getenv('makersuite')

@app.route("/", methods = ["GET", "POST"])
def index():
    return(render_template("index.html"))

@app.route("/main", methods = ["GET", "POST"])
def main():
    name = request.form.get("q")
    return(render_template("main.html"))

@app.route("/SA", methods = ["GET", "POST"])
def SA():
    return(render_template("SA.html"))

@app.route("/SA_result", methods = ["GET", "POST"])
def SA_result():
    q = request.form.get("q")
    r = textblob.TextBlob(q).sentiment
    
    return(render_template("SA_result.html", r=r))

@app.route("/genAI", methods = ["GET", "POST"])
def genAI():
    return(render_template("genAI.html"))

@app.route("/genAI_result", methods = ["GET", "POST"])
def genAI_result():
    q = request.form.get("q")
    genai.configure(api_key=api)
    model = genai.GenerativeModel("gemini-1.5-flash")
    r = model.generate_content(q)
    r = r.candidates[0].content.parts[0].text
    return(render_template("genAI_result.html", r=r))

if __name__ == "__main__":
    app.run(port=1234)