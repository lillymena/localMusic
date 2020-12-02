from app import db


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
