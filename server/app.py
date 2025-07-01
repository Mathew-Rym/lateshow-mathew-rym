from flask import Flask
from flask_migrate import Migrate
from models import db,bcrypt
from config import Config
from flask_restful import Api
from controllers import Home,Register,Login,Logout,CheckSession,EpisodeResource,EpisodeByIdResource,GuestResource,AppearanceResource


app = Flask(__name__)
api = Api(app)
app.config.from_object(Config)

bcrypt.init_app(app)
db.init_app(app)
migrate = Migrate(app,db)

api.add_resource(Home, '/')
api.add_resource(Register, '/register')
api.add_resource(Login, '/login')
api.add_resource(Logout, '/logout')
api.add_resource(CheckSession, '/check_session')
api.add_resource(EpisodeResource, '/episodes')
api.add_resource(EpisodeByIdResource,'/episodes/<int:id>')
api.add_resource(GuestResource, '/guests')
api.add_resource(AppearanceResource,'/appearances')


if __name__ == '__main__':
    app.run(port=5555)


