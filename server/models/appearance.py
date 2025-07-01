from . import db,SerializerMixin,validates


class Appearance(db.Model, SerializerMixin):
    __tablename__ = 'appearances'
    
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer)
    guest_id = db.Column(db.Integer, db.ForeignKey('guests.id'))
    episode_id = db.Column(db.Integer, db.ForeignKey('episodes.id'))
    
    guest = db.relationship('Guest', back_populates='appearances')
    episode = db.relationship('Episode', back_populates='appearances')
    
    serialize_rules =('-episode.appearances','-guest.appearances')
    
    def __repr__(self):
        return f'<Appearance {self.rating}, {self.id}>'
    
    validates('rating')
    def validate_rating(self,key,rating):
        if rating in [1,2,3,4,5]:
            return rating
        else:
            raise ValueError('Rating must be between 1-5')