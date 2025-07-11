from . import db,SerializerMixin,validates,bcrypt
from sqlalchemy.ext.hybrid import hybrid_property


class User(db.Model, SerializerMixin):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False, unique=True)
    _password_hash = db.Column(db.String,nullable=False)
    
    
    def __repr__(self):
        return f'<User {self.username}, {self.id}>'
    
    @validates('username')
    def validate_username(self,key,username):
        if not username:
            raise ValueError('Username must not be empty')
        if User.query.filter(User.username == username).first():
            raise ValueError('Username must be unique')
        
        return username
        
    @hybrid_property
    def password_hash(self):
        return self._password_hash
    
    @password_hash.setter
    def password_hash(self, password):
        password_hash = bcrypt.generate_password_hash(
            password.encode('utf-8'))
        self._password_hash = password_hash.decode('utf-8')
        
    def authenticate(self,password):
        return bcrypt.check_password_hash(
            self._password_hash, password.encode('utf-8'))