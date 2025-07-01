from . import make_response,Resource,request,User,IntegrityError,session
from models import db 


class Home(Resource):
    def get(self):
        return make_response('<h1>Welcome to Late Show Api</h1>',200)



class Register(Resource):
    def post(self):
        data = request.get_json()
        try:
            new_user =User(
                username = data['username'],
                password_hash =data['password']
            )
            db.session.add(new_user)
            db.session.commit()
            
            session['user_id'] = new_user.id
            
            response = {
                'id':new_user.id,
                'username':new_user.username
            } 
            return make_response(
                response,
                201
            )
        except IntegrityError:
            db.session.rollback()
            response ={
                'errors':['422 Unprocessable Entity']
            }
            return make_response(
                response,
                422
            )
            
        except KeyError:
            db.session.rollback()
            response ={
                'errors':['422 Unprocessable Entity']
            }
            return make_response(
                response,
                422
            )
            
class Login(Resource):
    def post(self):
        data = request.get_json()
        username = data['username']
        password = data['password']
        
        if not username or not password:
            return make_response({'message':'Missing username or password'},400)
        
        user = User.query.filter(User.username == username).first()
        if user and user.authenticate(password):
            session['user_id']=user.id
            response ={
                'id':user.id,
                'username':user.username,
                'login_successful':True
            }
            return make_response(
                response,
                200
            )
        
        return make_response(
            {'error':'Unauthorized'},
            401
        )
        
class Logout(Resource):
    def delete(self):
        if session['user_id']:
            session['user_id'] = None
            return make_response(
                {'message':'Successfully logged out. See you later.'},
                204
            )
        return make_response(
            {'error':'You are not logged in'},
            401
        )
        

class CheckSession(Resource):
    def get(self):
        user_id = session['user_id']
        user = User.query.filter(User.id == user_id).first()
        
        if user:
            response ={
                'id': user.id,
                'username':user.username,
                'logged_in': True
            }
            return make_response(
                response,
                200
            )
        return make_response(
            {'message':'You are not logged in'},
            401
        )
        
