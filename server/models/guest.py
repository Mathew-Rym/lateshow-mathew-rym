from . import db,SerializerMixin


class Guest(db.Model, SerializerMixin):
    __tablename__ = 'guests'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    occupation = db.Column(db.String)
    
    appearances = db.relationship('Appearance', back_populates='guest', cascade='all, delete-orphan')
    
    serialize_rules =('-appearances.guest',)
    
    def __repr__(self):
        return f'<Guest {self.name}, {self.occupation}>'