from flask import render_template
from app import app


@app.route('/')
@app.route('/home')
def homepage():
    title = {'title': 'welcome to my local music database'}
    body = {'body': 'come find out about my current favorite artists :)'}
    return render_template('base.html', title='home', user=title, body=body)


@app.route('/artists')
def listOfArtists():
    title = {'title': 'this is a list of my favorite artists'}
    body = {'artist': 'SIR'}, {'artist': 'Smino'}, {'artist': 'SZA'}
    return render_template('localArtist.html', title='home', user=title, body=body)


@app.route('/newArtist')
def createNewArtist():
    title = {'title': 'New Artists'}
    body = {'artist'}
    return render_template('newArtist.html', title='home', user=title, body=body)


@app.route('/sir')
def sir():
    title = {'title': 'This is Sir'}
    body = {''}
    return render_template('sir.html', title='home', user=title, body=body)
