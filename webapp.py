from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json

app = Flask(__name__)

with open('drugs.json') as drug_data:
    drugs = json.load(drug_data)


@app.route('/')
def render_mainpage():
    return render_template('mainpage.html')


@app.route('/page1' )
def render_page1():

    if 'state' in request.args:
        state = request.args['state']
    else:

        state = 'State...'
    return render_template(
        'page1.html',
        options1=get_all_states(drugs),
        selectedState=state,
        overallpop=pop_by_state(drugs, state),
        newMarP=newMarP_by_state(drugs, state),
        monMarP=monMarP_by_state(drugs, state),
        yearMarP=yearMarP_by_state(drugs, state),
        perMarP=perMarP_by_state(drugs, state),
        newTobP=newTobP_by_state(drugs, state),
        monTobP=monTobP_by_state(drugs, state),
        perTobP=perTobP_by_state(drugs, state),
        abuAlcP=abuAlcP_by_state(drugs, state),
        monAlcP=monAlcP_by_state(drugs, state),
        perAlcP=perAlcP_by_state(drugs, state),
        depAlcP=depAlcP_by_state(drugs, state),
        treAlcP=treAlcP_by_state(drugs, state),
        newMarO=newMarO_by_state(drugs, state),
        monMarO=monMarO_by_state(drugs, state),
        yearMarO=yearMarO_by_state(drugs, state),
        perMarO=perMarO_by_state(drugs, state),
        newTobO=newTobO_by_state(drugs, state),
        monTobO=monTobO_by_state(drugs, state),
        perTobO=perTobO_by_state(drugs, state),
        abuAlcO=abuAlcO_by_state(drugs, state),
        monAlcO=monAlcO_by_state(drugs, state),
        perAlcO=perAlcO_by_state(drugs, state),
        depAlcO=depAlcO_by_state(drugs, state),
        treAlcO=treAlcO_by_state(drugs, state),
        )


def get_all_states(drugs):
    options1 = ''
    listOfStates = []
    for x in drugs:
        if x['State'] not in listOfStates:
            listOfStates.append(x['State'])
    for x in listOfStates:
        options1 += Markup('<option value="' + x + '">' + x
                           + '</option>')
    return options1


def pop_by_state(drugs, state):
    for x in drugs:
        if state == x['State']:
            return 'Population of ' + state \
                + ' in 2002 over 12 years old: ' + str(x['Population'
                    ]['12-17'] + x['Population']['18-25']
                    + x['Population']['26+'])


def newMarP_by_state(drugs, state):
    for x in drugs:
        if state == x['State']:
            return 'New Marijuana users (past year): ' + str(x['Totals'
                    ]['Marijuana']['New Users']['12-17'] + x['Totals'
                    ]['Marijuana']['New Users']['18-25'] + x['Totals'
                    ]['Marijuana']['New Users']['26+'])


def monMarP_by_state(drugs, state):
    for x in drugs:
        if state == x['State']:
            return 'Marijuana use past month: ' + str(x['Totals'
                    ]['Marijuana']['Used Past Month']['12-17']
                    + x['Totals']['Marijuana']['Used Past Month'
                    ]['18-25'] + x['Totals']['Marijuana'
                    ]['Used Past Month']['26+'])


def yearMarP_by_state(drugs, state):
    for x in drugs:
        if state == x['State']:
            return 'Marijuana use past year: ' + str(x['Totals'
                    ]['Marijuana']['Used Past Year']['12-17']
                    + x['Totals']['Marijuana']['Used Past Year']['18-25'
                    ] + x['Totals']['Marijuana']['Used Past Year']['26+'
                    ])


def perMarP_by_state(drugs, state):
    for x in drugs:
        if state == x['State']:
            return 'Populations Marijuana perception of risk: ' \
                + str(x['Totals']['Marijuana']['Perceptions of Risk'
                      ]['12-17'] + x['Totals']['Marijuana'
                      ]['Perceptions of Risk']['18-25'] + x['Totals'
                      ]['Marijuana']['Perceptions of Risk']['26+'])


def newTobP_by_state(drugs, state):
    for x in drugs:
        if state == x['State']:
            return 'New Tobacco users (past year): ' + str(x['Totals'
                    ]['Tobacco']['Cigarette Past Month']['12-17']
                    + x['Totals']['Tobacco']['Cigarette Past Month'
                    ]['18-25'] + x['Totals']['Tobacco'
                    ]['Cigarette Past Month']['26+'])


def monTobP_by_state(drugs, state):
    for x in drugs:
        if state == x['State']:
            return 'Tobacco use past month: ' + str(x['Totals'
                    ]['Tobacco']['Use Past Month']['12-17'] + x['Totals'
                    ]['Tobacco']['Use Past Month']['18-25'] + x['Totals'
                    ]['Tobacco']['Use Past Month']['26+'])


def perTobP_by_state(drugs, state):
    for x in drugs:
        if state == x['State']:
            return 'Populations Tobacco perception of risk: ' \
                + str(x['Totals']['Tobacco']['Perceptions of Risk'
                      ]['12-17'] + x['Totals']['Tobacco'
                      ]['Perceptions of Risk']['18-25'] + x['Totals'
                      ]['Tobacco']['Perceptions of Risk']['26+'])


def abuAlcP_by_state(drugs, state):
    for x in drugs:
        if state == x['State']:
            return 'Alcohol abuse (past year): ' + str(x['Totals'
                    ]['Alcohol']['Abuse Past Year']['12-17']
                    + x['Totals']['Alcohol']['Abuse Past Year']['18-25'
                    ] + x['Totals']['Alcohol']['Abuse Past Year']['26+'
                    ])


def depAlcP_by_state(drugs, state):
    for x in drugs:
        if state == x['State']:
            return 'Alcohol dependency: ' + str(x['Totals']['Alcohol'
                    ]['Dependence Past Year']['12-17'] + x['Totals'
                    ]['Alcohol']['Dependence Past Year']['18-25']
                    + x['Totals']['Alcohol']['Dependence Past Year'
                    ]['26+'])


def monAlcP_by_state(drugs, state):
    for x in drugs:
        if state == x['State']:
            return 'Monthly Alcohol use : ' + str(x['Totals']['Alcohol'
                    ]['Use Past Month']['12-17'] + x['Totals']['Alcohol'
                    ]['Use Past Month']['18-25'] + x['Totals']['Alcohol'
                    ]['Use Past Month']['26+'])


def perAlcP_by_state(drugs, state):
    for x in drugs:
        if state == x['State']:
            return 'Populations Alcohol perception of risk: ' \
                + str(x['Totals']['Alcohol']['Perceptions of Risk'
                      ]['12-17'] + x['Totals']['Alcohol'
                      ]['Perceptions of Risk']['18-25'] + x['Totals'
                      ]['Alcohol']['Perceptions of Risk']['26+'])


def treAlcP_by_state(drugs, state):
    for x in drugs:
        if state == x['State']:
            return 'Need Treatment for Alcohol (past year): ' \
                + str(x['Totals']['Alcohol']['Need Treatment Past Year'
                      ]['12-17'] + x['Totals']['Alcohol'
                      ]['Need Treatment Past Year']['18-25']
                      + x['Totals']['Alcohol'
                      ]['Need Treatment Past Year']['26+'])


def newMarO_by_state(drugs, state):
    for x in drugs:
        if state == x['State']:
            return 'New Marijuana users (past year): ' \
                + str(round((x['Rates']['Marijuana']['New Users'
                      ]['12-17'] + x['Rates']['Marijuana']['New Users'
                      ]['18-25'] + x['Rates']['Marijuana']['New Users'
                      ]['26+']) / 3, 3))


def monMarO_by_state(drugs, state):
    for x in drugs:
        if state == x['State']:
            return 'Marijuana use past month: ' + str(round((x['Rates'
                    ]['Marijuana']['Used Past Month']['12-17']
                    + x['Rates']['Marijuana']['Used Past Month']['18-25'
                    ] + x['Rates']['Marijuana']['Used Past Month']['26+'
                    ]) / 3, 3))


def yearMarO_by_state(drugs, state):
    for x in drugs:
        if state == x['State']:
            return 'Marijuana use past year: ' + str(round((x['Rates'
                    ]['Marijuana']['Used Past Year']['12-17']
                    + x['Rates']['Marijuana']['Used Past Year']['18-25'
                    ] + x['Rates']['Marijuana']['Used Past Year']['26+'
                    ]) / 3, 3))


def perMarO_by_state(drugs, state):
    for x in drugs:
        if state == x['State']:
            return 'Populations Marijuana perception of risk: ' \
                + str(round((x['Rates']['Marijuana'
                      ]['Perceptions of Risk']['12-17'] + x['Rates'
                      ]['Marijuana']['Perceptions of Risk']['18-25']
                      + x['Rates']['Marijuana']['Perceptions of Risk'
                      ]['26+']) / 3, 3))


def newTobO_by_state(drugs, state):
    for x in drugs:
        if state == x['State']:
            return 'New Tobacco users (past year): ' \
                + str(round((x['Rates']['Tobacco'
                      ]['Cigarette Past Month']['12-17'] + x['Rates'
                      ]['Tobacco']['Cigarette Past Month']['18-25']
                      + x['Rates']['Tobacco']['Cigarette Past Month'
                      ]['26+']) / 3, 3))


def monTobO_by_state(drugs, state):
    for x in drugs:
        if state == x['State']:
            return 'Tobacco use past month: ' + str(round((x['Rates'
                    ]['Tobacco']['Use Past Month']['12-17'] + x['Rates'
                    ]['Tobacco']['Use Past Month']['18-25'] + x['Rates'
                    ]['Tobacco']['Use Past Month']['26+']) / 3, 3))


def perTobO_by_state(drugs, state):
    for x in drugs:
        if state == x['State']:
            return 'Populations Tobacco perception of risk: ' \
                + str(round((x['Rates']['Tobacco']['Perceptions of Risk'
                      ]['12-17'] + x['Rates']['Tobacco'
                      ]['Perceptions of Risk']['18-25'] + x['Rates'
                      ]['Tobacco']['Perceptions of Risk']['26+']) / 3,
                      3))


def abuAlcO_by_state(drugs, state):
    for x in drugs:
        if state == x['State']:
            return 'Alcohol abuse (past year): ' + str(round((x['Rates'
                    ]['Alcohol']['Abuse Past Year']['12-17'] + x['Rates'
                    ]['Alcohol']['Abuse Past Year']['18-25'] + x['Rates'
                    ]['Alcohol']['Abuse Past Year']['26+']) / 3, 3))


def depAlcO_by_state(drugs, state):
    for x in drugs:
        if state == x['State']:
            return 'Alcohol dependency: ' + str(round((x['Rates'
                    ]['Alcohol']['Dependence Past Year']['12-17']
                    + x['Rates']['Alcohol']['Dependence Past Year'
                    ]['18-25'] + x['Rates']['Alcohol'
                    ]['Dependence Past Year']['26+']) / 3, 3))


def monAlcO_by_state(drugs, state):
    for x in drugs:
        if state == x['State']:
            return 'Monthly Alcohol use : ' + str(round((x['Rates'
                    ]['Alcohol']['Use Past Month']['12-17'] + x['Rates'
                    ]['Alcohol']['Use Past Month']['18-25'] + x['Rates'
                    ]['Alcohol']['Use Past Month']['26+']) / 3, 3))


def perAlcO_by_state(drugs, state):
    for x in drugs:
        if state == x['State']:
            return 'Populations Alcohol perception of risk: ' \
                + str(round((x['Rates']['Alcohol']['Perceptions of Risk'
                      ]['12-17'] + x['Rates']['Alcohol'
                      ]['Perceptions of Risk']['18-25'] + x['Rates'
                      ]['Alcohol']['Perceptions of Risk']['26+']) / 3,
                      3))


def treAlcO_by_state(drugs, state):
    for x in drugs:
        if state == x['State']:
            return 'Need Treatment for Alcohol (past year): ' \
                + str(round((x['Rates']['Alcohol'
                      ]['Need Treatment Past Year']['12-17'] + x['Rates'
                      ]['Alcohol']['Need Treatment Past Year']['18-25']
                      + x['Rates']['Alcohol']['Need Treatment Past Year'
                      ]['26+']) / 3, 3))


@app.route('/page2')
def render_page2():
    if 'rate' in request.args:
        rate = request.args['rate']
    else:
        rate = 'Rate...'
    return render_template('page2.html',options2=find_rates(drugs), data=get_data(drugs,rate))

def find_rates(drugs):
    options2 = ''
    listOfRates = []
    for x in drugs[0]["Rates"]["Illicit Drugs"]:
        if x not in listOfRates:
            listOfRates.append(str("Illicit Drugs " + x))
        options2 += Markup('<option value="' + x + '">' + x
                           + '</option>')
    return options2

def get_data(drugs,rate):
    fit=-1
    oneN=-1
    oneS="error"
    twoN=-1
    twoS="error"
    threeN=-1
    threeS="error"
    fourN=-1
    fourS="error"
    fiveN=-1
    fiveS="error"
    sixN=-1
    sixS="error"
    sevenN=-1
    sevenS="error"
    eightN=-1
    eightS="error"
    nineN=-1
    nineS="error"
    tenN=-1
    tenS="error"
    elevenN=-1
    elevenS="error"
    twelveN=-1
    twelveS="error"
    thirteenN=-1
    thirteenS="error"
    fourteenN=-1
    fourteenS="error"
    fifteenN=-1
    fifteenS="error"
    for x in drugs:
        if x["Year"]==2002:
            fit=x["Rates"]["Illicit Drugs"][rate]["26+"]
            print(fit)
            if float(fit) > float(oneN): #or any of the others
                fifteenN=fourteenN
                fifteenS=fourteenS
                fourteenN=thirteenN
                fourteenS=thirteenS
                thirteenN=twelveN
                thirteenS=twelveS
                twelveN=elevenN
                twelveS=tenS
                elevenN=tenN
                elevenS=tenS
                tenN=nineN
                tenS=nineS
                nineN=eightN
                nineS=eightS
                eightN=sevenN
                eightS=sevenS
                sevenN=sixN
                sevenS=sixS
                sixN=fiveN
                sixS=fiveS
                fiveN=fourN
                fiveS=fourS
                fourN=threeN
                fourS=threeS
                threeN=twoN
                threeS=twoS
                twoN=oneN
                twoS=oneS
                oneN=fit
                oneS=x["State"]
            else:
                if float(fit) > float(twoN): #or any of the others
                    fifteenN=fourteenN
                    fifteenS=fourteenS
                    fourteenN=thirteenN
                    fourteenS=thirteenS
                    thirteenN=twelveN
                    thirteenS=twelveS
                    twelveN=elevenN
                    twelveS=tenS
                    elevenN=tenN
                    elevenS=tenS
                    tenN=nineN
                    tenS=nineS
                    nineN=eightN
                    nineS=eightS
                    eightN=sevenN
                    eightS=sevenS
                    sevenN=sixN
                    sevenS=sixS
                    sixN=fiveN
                    sixS=fiveS
                    fiveN=fourN
                    fiveS=fourS
                    fourN=threeN
                    fourS=threeS
                    threeN=twoN
                    threeS=twoS
                    twoN=oneN
                    twoS=x["State"]
    return Markup('{ y: %s, label: "%s" },{ y: %s, label: "%s" },{ y: %s, label: "%s" },{ y: %s, label: "%s" },{ y: %s, label: "%s" },{ y: %s, label: "%s" },{ y: %s, label: "%s" },{ y: %s, label: "%s" },{ y: %s, label: "%s" },{ y: %s, label: "%s" },{ y: %s, label: "%s" },{ y: %s, label: "%s" },{ y: %s, label: "%s" },{ y: %s, label: "%s" },{ y: %s, label: "%s" }' % (oneN,oneS,twoN,twoS,threeN,threeS,fourN,fourS,fiveN,fiveS,sixN,sixS,sevenN,sevenS,eightN,eightS,nineN,nineS,tenN,tenS,elevenN,elevenS,twelveN,twelveS,thirteenN,thirteenS,fourteenN,fourteenS,fifteenN,fifteenS))


if __name__ == '__main__':
    app.run(debug=True, port=54321)
