from flask import Flask
from smartlights.app.lightsapp import lights

app = Flask(__name__)
app.register_blueprint(lights)

from flask_restful import Api
from smartlights.api.lightsapi import LightList, Light, Ping

api = Api(app)
api.add_resource(Ping, "/api/v1/ping", endpoint="Ping")
api.add_resource(LightList, "/api/v1/lights", endpoint="AllLights")
api.add_resource(Light, "/api/v1/lights/<string:lightId>", endpoint="LightById")
api.add_resource(Light, "/api/v1/lights/<string:lightId>/<string:action>", endpoint="TriggerLight")
