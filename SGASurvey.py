from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Response

app = Flask(__name__)

engine = create_engine('sqlite:///Survey.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/')
def landing():
    return render_template('landing.html')

@app.route('/survey', methods = ['GET','POST'])
def surveyAnswer():
    if request.method == 'POST':
        newResponse=Response(q1=request.form['q1'],q2=request.form['q2'],q3=request.form['q3'],q4=request.form['q4'],q5=request.form['q5'],comments=request.form['comments'])
        session.add(newResponse)
        session.commit()
        flash("Thank you for filling out the form!")
        return redirect(url_for('landing'))
    else:
        return render_template('survey.html')

@app.route('/answers')
def answerPage():
        return render_template('answers.html')

@app.route('/replies/JSON')
def repliesJson():
    replies = session.query(Response)
    return jsonify(Responses=[i.serialize for i in replies])

if __name__ == '__main__':
    app.secret_key = 'SGAisCool'
    app.debug = True
    app.run(host='0.0.0.0', port=8080)
