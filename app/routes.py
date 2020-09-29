from flask import render_template, flash
from app import app
from app.templates.forms import NewArtist


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


@app.route('/newArtist', methods=['GET', 'POST'])
def createNewArtist():
    form = NewArtist()
    if form.validate_on_submit():
        flash("New Artist Request Submitted".format)
        new_form = NewArtist()
        render_template('newArtist.html', title="New Artist Request", form=new_form)

    return render_template('newArtist.html', title="New Artist Request", form=form)


@app.route('/sir')
def sir():
    title = {'title': 'This is Sir'}
    body = {''}
    return render_template('sir.html', title='home', user=title, body=body)