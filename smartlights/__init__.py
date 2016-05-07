from flask import Flask
from smartlights.app.lightsapp import lightsapp

app = Flask(__name__)
app.register_blueprint(lightsapp)

from flask_restful import Api
from smartlights.api.lightsapi import LightList, Light

api = Api(app)
api.add_resource(LightList, "/api/v1/lights", endpoint="AllLights")
api.add_resource(Light, "/api/v1/lights/<string:lightId>", endpoint="LightById")
api.add_resource(Light, "/api/v1/lights/<string:lightId>/<string:action>", endpoint="TriggerLight")
