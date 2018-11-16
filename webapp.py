from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json

app = Flask(__name__)

@app.route("/")
def render_mainpage():
  return render_template("mainpage.html")
  
@app.route("/page1")
def render_page1():
  return render_template("page1.html")

if __name__=="__main__":
    app.run(debug=True, port=54321)
