from . import make_response,Resource,Episode,session
from models import db 

class EpisodeResource(Resource):
    def get(self):
        episodes_dict = [episode.to_dict() for episode in Episode.query.all()]
        return make_response(
            episodes_dict,
            200
        )
        
class EpisodeByIdResource(Resource):
    def get(self, id):
        episode = Episode.query.filter(Episode.id == id).first()
        if not episode:
            return make_response(
                {'message':f'Episode with id {id} does not exists'}
            )  
  
        return make_response(
            episode.to_dict(),
            200
        )
    
    def delete(self, id):
        user_id = session['user_id']
        if not user_id:
            return make_response(
                {'error':'Unauthorized'},
                401
            )
            
        episode = Episode.query.filter(Episode.id == id).first()
        if episode:
            db.session.delete(episode)
            db.session.commit()
            
            return make_response(
                {
                    'deleted_successfully':True,
                    'message': 'Deletion successful'
                },
                200
            )
        return make_response(
                {'message':f'Episode with id {id} does not exists'}
            )  
    