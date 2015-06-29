from app import db


class Board(db.Model):
    __tablename__ = 'boards'

    id = db.Column(db.Integer, primary_key=True)
    shortname = db.Column(db.String(10), nullable=False, unique=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Unicode(200))

    def __init__(self, shortname, name, description=u''):
        self.shortname = shortname
        self.name = name
        self.description = description

    def __repr__(self):
        return '<id {}>: <{} - {}>'.format(self.id, self.shortname, self.name)

    @property
    def serialize(self):
        return {
            'shortname': self.shortname,
            'name': self.name,
            'description': self.description
        }
