from . import db,SerializerMixin


class Episode(db.Model, SerializerMixin):
    __tablename__ = 'episodes'
    
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    number = db.Column(db.Integer)
    
    appearances = db.relationship('Appearance', back_populates='episode',cascade='all, delete-orphan')
    
    serialize_rules =('-appearances.episode',)

    
    def __repr__(self):
        return f'<Episode {self.number}, {self.date}>'