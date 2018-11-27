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
        return render_template("page1.html" , options1=get_all_states(drugs) , selectedState=state, overallpop=pop_by_state(drugs,state), newMar=newMar_by_state(drugs,state) , monMar=monMar_by_state(drugs,state) , yearMar=yearMar_by_state(drugs,state) , perMar=perMar_by_state(drugs,state) , newTob=newTob_by_state(drugs,state) , monTob=monTob_by_state(drugs,state) , yearTob=yearTob_by_state(drugs,state) , perTob=perTob_by_state(drugs,state))
    else:
        return render_template("page1.html" , options1=get_all_states(drugs))

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

def newMar_by_state(drugs,state):
    for x in drugs:
        if state==x["State"]:
            return "New Marijuana users (past year): " + str(x["Totals"]["Marijuana"]["New Users"]["12-17"] + x["Totals"]["Marijuana"]["New Users"]["18-25"] + x["Totals"]["Marijuana"]["New Users"]["26+"])

def monMar_by_state(drugs,state):
    for x in drugs:
        if state==x["State"]:
            return "Marijuana use past month: " + str(x["Totals"]["Marijuana"]["Used Past Month"]["12-17"] + x["Totals"]["Marijuana"]["Used Past Month"]["18-25"] + x["Totals"]["Marijuana"]["Used Past Month"]["26+"])            

def yearMar_by_state(drugs,state):
    for x in drugs:
        if state==x["State"]:
            return "Marijuana use past year: " + str(x["Totals"]["Marijuana"]["Used Past Year"]["12-17"] + x["Totals"]["Marijuana"]["Used Past Year"]["18-25"] + x["Totals"]["Marijuana"]["Used Past Year"]["26+"])            
            
def perMar_by_state(drugs,state):
    for x in drugs:
        if state==x["State"]:
            return "Populations Marijuana perception of risk: " + str(x["Totals"]["Marijuana"]["Perceptions of Risk"]["12-17"] + x["Totals"]["Marijuana"]["Perceptions of Risk"]["18-25"] + x["Totals"]["Marijuana"]["Perceptions of Risk"]["26+"])            

def newTob_by_state(drugs,state):
    for x in drugs:
        if state==x["State"]:
            return "New Tobacco users (past year): " + str(x["Totals"]["Tobacco"]["New Users"]["12-17"] + x["Totals"]["Marijuana"]["New Users"]["18-25"] + x["Totals"]["Marijuana"]["New Users"]["26+"])

def monTob_by_state(drugs,state):
    for x in drugs:
        if state==x["State"]:
            return "Tobacco use past month: " + str(x["Totals"]["Marijuana"]["Used Past Month"]["12-17"] + x["Totals"]["Marijuana"]["Used Past Month"]["18-25"] + x["Totals"]["Marijuana"]["Used Past Month"]["26+"])            

def yearTob_by_state(drugs,state):
    for x in drugs:
        if state==x["State"]:
            return "Tobacco use past year: " + str(x["Totals"]["Marijuana"]["Used Past Year"]["12-17"] + x["Totals"]["Marijuana"]["Used Past Year"]["18-25"] + x["Totals"]["Marijuana"]["Used Past Year"]["26+"])            
            
def perTob_by_state(drugs,state):
    for x in drugs:
        if state==x["State"]:
            return "Populations Tobacco perception of risk: " + str(x["Totals"]["Marijuana"]["Perceptions of Risk"]["12-17"] + x["Totals"]["Marijuana"]["Perceptions of Risk"]["18-25"] + x["Totals"]["Marijuana"]["Perceptions of Risk"]["26+"])            

if __name__=="__main__":
    app.run(debug=True, port=54321)
