from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json

app = Flask(__name__)

@app.route("/")
def render_mainpage():
  return render_template("mainpage.html")

@app.route("/page1")
def render_page1():
    with open('drugs.json') as drug_data:
        drugs = json.load(drug_data)
    if "state" in request.args:
        state = request.args['state']
        return render_template("page1.html" , options1=get_all_states(drugs) , selectedState=state, overallpop=pop_by_state(drugs,state) , 
        newMarP=newMarP_by_state(drugs,state) , monMarP=monMarP_by_state(drugs,state) , yearMarP=yearMarP_by_state(drugs,state) , perMarP=perMarP_by_state(drugs,state) , 
        newTobP=newTobP_by_state(drugs,state) , monTobP=monTobP_by_state(drugs,state) , perTobP=perTobP_by_state(drugs,state) ,
        abuAlcP=abuAlcP_by_state(drugs,state) , monAlcP=monAlcP_by_state(drugs,state) , perAlcP=perAlcP_by_state(drugs,state) , depAlcP=depAlcP_by_state(drugs,state) , treAlcP=treAlcP_by_state(drugs,state))
    else:
        state="State..."
        return render_template("page1.html" , options1=get_all_states(drugs) , selectedState="State...", overallpop=pop_by_state(drugs,state) , 
        newMarP=newMarP_by_state(drugs,state) , monMarP=monMarP_by_state(drugs,state) , yearMarP=yearMarP_by_state(drugs,state) , perMarP=perMarP_by_state(drugs,state) , 
        newTobP=newTobP_by_state(drugs,state) , monTobP=monTobP_by_state(drugs,state) , perTobP=perTobP_by_state(drugs,state) ,
        abuAlcP=abuAlcP_by_state(drugs,state) , monAlcP=monAlcP_by_state(drugs,state) , perAlcP=perAlcP_by_state(drugs,state) , depAlcP=depAlcP_by_state(drugs,state) , treAlcP=treAlcP_by_state(drugs,state))

def get_all_states(drugs):
    options1=""
    listOfStates=[]
    for x in drugs:
        if x["State"] not in listOfStates:
            listOfStates.append(x["State"])
    for x in listOfStates:
        options1 += Markup("<option value=\"" + x + "\">" + x + "</option>")
    return options1

def pop_by_state(drugs,state):
    for x in drugs:
        if state==x["State"]:
            return "Population of " + state + " in 2002 over 12 years old: " + str(x["Population"]["12-17"] + x["Population"]["18-25"] + x["Population"]["26+"])

            
            
def newMarP_by_state(drugs,state):
    for x in drugs:
        if state==x["State"]:
            return "New Marijuana users (past year): " + str(x["Totals"]["Marijuana"]["New Users"]["12-17"] + x["Totals"]["Marijuana"]["New Users"]["18-25"] + x["Totals"]["Marijuana"]["New Users"]["26+"])

def monMarP_by_state(drugs,state):
    for x in drugs:
        if state==x["State"]:
            return "Marijuana use past month: " + str(x["Totals"]["Marijuana"]["Used Past Month"]["12-17"] + x["Totals"]["Marijuana"]["Used Past Month"]["18-25"] + x["Totals"]["Marijuana"]["Used Past Month"]["26+"])

def yearMarP_by_state(drugs,state):
    for x in drugs:
        if state==x["State"]:
            return "Marijuana use past year: " + str(x["Totals"]["Marijuana"]["Used Past Year"]["12-17"] + x["Totals"]["Marijuana"]["Used Past Year"]["18-25"] + x["Totals"]["Marijuana"]["Used Past Year"]["26+"])
            
def perMarP_by_state(drugs,state):
    for x in drugs:
        if state==x["State"]:
            return "Populations Marijuana perception of risk: " + str(x["Totals"]["Marijuana"]["Perceptions of Risk"]["12-17"] + x["Totals"]["Marijuana"]["Perceptions of Risk"]["18-25"] + x["Totals"]["Marijuana"]["Perceptions of Risk"]["26+"])

            
            
def newTobP_by_state(drugs,state):
    for x in drugs:
        if state==x["State"]:
            return "New Tobacco users (past year): " + str(x["Totals"]["Tobacco"]["Cigarette Past Month"]["12-17"] + x["Totals"]["Tobacco"]["Cigarette Past Month"]["18-25"] + x["Totals"]["Tobacco"]["Cigarette Past Month"]["26+"])

def monTobP_by_state(drugs,state):
    for x in drugs:
        if state==x["State"]:
            return "Tobacco use past month: " + str(x["Totals"]["Tobacco"]["Use Past Month"]["12-17"] + x["Totals"]["Tobacco"]["Use Past Month"]["18-25"] + x["Totals"]["Tobacco"]["Use Past Month"]["26+"])
            
def perTobP_by_state(drugs,state):
    for x in drugs:
        if state==x["State"]:
            return "Populations Tobacco perception of risk: " + str(x["Totals"]["Tobacco"]["Perceptions of Risk"]["12-17"] + x["Totals"]["Tobacco"]["Perceptions of Risk"]["18-25"] + x["Totals"]["Tobacco"]["Perceptions of Risk"]["26+"])

            
            
def abuAlcP_by_state(drugs,state):
    for x in drugs:
        if state==x["State"]:
            return "Alcohol abuse (past year): " + str(x["Totals"]["Alcohol"]["Abuse Past Year"]["12-17"] + x["Totals"]["Alcohol"]["Abuse Past Year"]["18-25"] + x["Totals"]["Alcohol"]["Abuse Past Year"]["26+"])

def depAlcP_by_state(drugs,state):
    for x in drugs:
        if state==x["State"]:
            return "Alcohol dependency: " + str(x["Totals"]["Alcohol"]["Dependence Past Year"]["12-17"] + x["Totals"]["Alcohol"]["Dependence Past Year"]["18-25"] + x["Totals"]["Alcohol"]["Dependence Past Year"]["26+"])

def monAlcP_by_state(drugs,state):
    for x in drugs:
        if state==x["State"]:
            return "Monthly Alcohol use : " + str(x["Totals"]["Alcohol"]["Use Past Month"]["12-17"] + x["Totals"]["Alcohol"]["Use Past Month"]["18-25"] + x["Totals"]["Alcohol"]["Use Past Month"]["26+"])
            
def perAlcP_by_state(drugs,state):
    for x in drugs:
        if state==x["State"]:
            return "Populations Alcohol perception of risk: " + str(x["Totals"]["Alcohol"]["Perceptions of Risk"]["12-17"] + x["Totals"]["Alcohol"]["Perceptions of Risk"]["18-25"] + x["Totals"]["Alcohol"]["Perceptions of Risk"]["26+"])

def treAlcP_by_state(drugs,state):
    for x in drugs:
        if state==x["State"]:
            return "Need Treatment for Alcohol (past year): " + str(x["Totals"]["Alcohol"]["Need Treatment Past Year"]["12-17"] + x["Totals"]["Alcohol"]["Need Treatment Past Year"]["18-25"] + x["Totals"]["Alcohol"]["Need Treatment Past Year"]["26+"])


if __name__=="__main__":
    app.run(debug=True, port=54321)
