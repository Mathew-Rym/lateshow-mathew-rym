from . import make_response,Resource,Appearance,request,IntegrityError,session
from models import db 

class AppearanceResource(Resource):
    def get(self):
        appearances_dict =[appearance.to_dict() for appearance in Appearance.query.all()]
        return make_response(
            appearances_dict,
            200
        )
        
    def post(self):
        user_id = session['user_id'] 
        if not user_id:
            return make_response(
                {'error':'Unauthorized'},
                401
            )
        
        data = request.get_json()
        try:
            new_post =Appearance(
                rating = data['rating'],
                guest_id = data['guest_id'],
                episode_id = data['episode_id'] 
            )
            db.session.add(new_post)
            db.session.commit()
            
            response = {
                'id':new_post.id,
                'rating':new_post.rating,
                'guest_id':new_post.guest_id,
                'episode_id':new_post.episode_id   
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

        