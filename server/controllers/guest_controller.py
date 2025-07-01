from . import make_response,Resource,Guest

class GuestResource(Resource):
    def get(self):
        guests_dict = [guest.to_dict() for guest in Guest.query.all()]
        return make_response(
            guests_dict,
            200
        )
        