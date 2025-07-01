from flask import make_response,request,session
from flask_restful import Resource
from models import Appearance,Episode,Guest,User
from sqlalchemy.exc import IntegrityError


from .auth_controller import Register,Login,Logout,CheckSession,Home
from .episode_controller import EpisodeResource,EpisodeByIdResource
from .guest_controller import GuestResource
from .appearance_controller import AppearanceResource