from flask import render_template, flash, redirect, url_for
from flask_login import current_user, login_user, logout_user, login_required

from app import app, db
from app.templates.forms import ArtistForm, LoginForm, RegistrationForm
from app.models import Artist, Venue, Event, ArtistToEvent, User


@app.route('/')
@app.route('/home')
def homepage():
    return render_template('index.html')


@app.route('/artists')
def listOfArtists():
    my_artists = Artist.query.all()
    if my_artists is None:
        return render_template('404.html')
    return render_template('artists.html', title='listOfArtists', artists=my_artists)


@app.route('/artist/<name>')
def artist(name):
    my_artist = Artist.query.filter_by(name=name).first()
    return render_template('artist.html', artist=my_artist)


@app.route('/newArtist', methods=['GET', 'POST'])
def createNewArtist():
    form = ArtistForm()
    if form.validate_on_submit():
        flash('New artist request {}'.format(form.name.data))
        my_artist = Artist(name=form.name.data, hometown=form.hometown.data, description=form.description.data)
        db.session.add(my_artist)
        db.session.commit()
        return redirect(url_for('listOfArtists'))
    return render_template('newArtist.html', title="newArtist", form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('homepage'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('homepage'))
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('homepage'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('login'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first()
    posts = [
        {'author': user, 'body': 'Test post #2'},
        {'author': user, 'body': 'Test post #2'}
    ]
    form = EmptyForm()
    return render_template('user.html', user=user, posts=posts, form=form)


@app.route('/reset_db')
def reset_db():
    flash("Resetting database: deleting old data and repopulating with dummy data")
    # clear all data from all tables
    meta = db.metadata
    for table in reversed(meta.sorted_tables):
        print('Clear table {}'.format(table))
        db.session.execute(table.delete())
    db.session.commit()

    a1 = Artist(name="Frank Ocean", hometown="Long Beach", description="Frank Ocean is known for his debut mixtape, "
                                                                       "'nostalgia, ULTRA,' and the subsequent albums"
                                                                       " 'channel ORANGE' and 'Blonde.")
    a2 = Artist(name="Sza", hometown="New Jersey", description="In October 2012, SZA self-released her debut EP, "
                                                               "See. SZA. Run, which she then followed up with her "
                                                               "second EP, S, in April 2013.")
    a3 = Artist(name="The Weeknd", hometown="Toronto", description="The Weeknd is known for his explicit songs about "
                                                                   "sex and drugs, many of which were "
                                                                   "autobiographical, and for his soaring falsetto "
                                                                   "and its singular tremolo.")

    v1 = Venue(name="Madison Square Garden", date="December 14th, 2021", location="New York City", tickets="5")
    v2 = Venue(name="Radio City Music Hall", date="March 28th, 2021", location="New York City", tickets="2")
    v3 = Venue(name="Hollywood Bowl", date="July 10th, 2021", location="Los Angeles", tickets="6")

    e1 = Event(name="Raclette Nights", date="December 14th, 2021", location="New York City", tickets="5")
    e2 = Event(name="Verdant Views", date="March 28th, 2021", location="New York City", tickets="2")
    e3 = Event(name="Virtual Entertainment", date="July 10th, 2021", location="Los Angeles", tickets="6")

    a2e1 = ArtistToEvent(artist=a1, event=e1)
    a2e2 = ArtistToEvent(artist=a1, event=e2)
    a2e3 = ArtistToEvent(artist=a2, event=e1)
    a2e4 = ArtistToEvent(artist=a3, event=e3)

    db.session.add_all([a1, a2, a3, v1, v2, v3, e1, e2, e3, a2e1, a2e2, a2e3, a2e4])
    db.session.commit()

    return redirect(url_for('homepage'))
