import datetime
from google.appengine.ext import db

class Session(db.Model):
	SessionName = db.StringProperty(required=True)

class Track(db.Model):
	session = db.ReferenceProperty(Session, collection_name='Tracks')
	TrackNumber = db.IntegerProperty(required=True)
	TrackName = db.StringProperty(required=True)
	TapeID = db.StringProperty(required=True)
	length = db.IntegerProperty(required=True)
	file = db.StringProperty(required=True)

class Artist(db.Model):
	track = db.ReferenceProperty(Track, collection_name='Artists')
	FirstName = db.StringProperty(required=True)
	LastName = db.StringProperty(required=True)

class Genre(db.Model):
	track = db.ReferenceProperty(Track, collection_name='Genres')
	GenreName = db.StringProperty(required=True)

a = Session(SessionName="Newport Folk Festival 1996");
a.put()

t = Track(session=a,
	TrackNumber=1,
	TrackName="Camera identification", 
	TapeID="N1R01",
	length=59,
	fileName="http://c0383352.cdn.cloudfiles.rackspacecloud.com/audio/N1R01.mp3" 
	).put()

Artist(track=t, 
	FirstName = 'Texas',
	LastName = 'Gladden'
	).put()

Genre (track=t,
	GenreName='Funk'
	).put()


print 'Content-Type: text/html'
print
for tracks in a.Tracks:
    print '%s: %s' % (tt.TrackNumber, tt.TrackName)
