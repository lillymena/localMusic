from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login


class Artist(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    hometown = db.Column(db.String)
    description = db.Column(db.String)
    artistToEvents = db.relationship("ArtistToEvent", backref="artist", lazy="dynamic")

    def __repr__(self):
        return "<Artist {} - {}>".format(self.id, self.name)


class Venue(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    date = db.Column(db.String)
    location = db.Column(db.String)
    tickets = db.Column(db.Integer)
    events = db.relationship("Event", backref="venue", lazy="dynamic")

    def __repr__(self):
        return "<Venue {} - {}>".format(self.id, self.name)


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    date = db.Column(db.String)
    location = db.Column(db.String)
    tickets = db.Column(db.Integer)
    venue_id = db.Column(db.Integer, db.ForeignKey('venue.id'))
    artistToEvents = db.relationship("ArtistToEvent", backref="event", lazy="dynamic")

    def __repr__(self):
        return "<Event {} - {}>".format(self.id, self.name)


class ArtistToEvent(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'))
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'))

    def __repr__(self):
        return "<ArtistToEvent {} - Artist {}, Event {}>".format(self.id, self.artist_id, self.event_id)


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))