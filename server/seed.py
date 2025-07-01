from app import app
from models import db,Appearance,Episode,Guest,User
import datetime

with app.app_context():
    print('Deleting existing records...')
    Appearance.query.delete()
    Episode.query.delete()
    Guest.query.delete()
    User.query.delete()
    db.session.commit()
    
    
    user = User(username='admin',password_hash='admin')
    
    db.session.add(user)
    
    
    guest1 = Guest(name ='Tom Cruise', occupation='Actor')
    guest2 = Guest(name ='Paul Pogba', occupation='Footballer')
    guest3 = Guest(name ='Stromae', occupation='Singer')
    
    db.session.add_all([guest1,guest2,guest3])
    
    episode1 = Episode(date=datetime.datetime(2025, 6, 20), number=1)
    episode2 = Episode(date=datetime.datetime(2025, 6, 21), number=2)

    
    db.session.add_all([episode1,episode2])
    
    appearance1 = Appearance(rating=5, guest=guest1, episode=episode1)
    appearance2 = Appearance(rating=3, guest=guest2, episode=episode1)
    appearance3 = Appearance(rating=4, guest=guest3, episode=episode2)
    appearance4 = Appearance(rating=5, guest=guest1, episode=episode2)
    
    db.session.add_all([appearance1,appearance2,appearance3,appearance4])
    
    db.session.commit()
    print('Successfully seeded database:)')
    
    
    
    