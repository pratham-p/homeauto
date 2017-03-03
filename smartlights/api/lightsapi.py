#!/usr/bin/env python3.4

#from flask import Blueprint
from flask import request
from flask_restful import Resource, reqparse
import subprocess, time, os

'''
lightsapi = Blueprint(
        'lightsapi',
        __name__
    )
'''

#app = Flask(__name__)
#api = Api(app)

#codeSendPath = os.path.join(os.path.abspath(os.curdir), "smarthome/smartlights")
codeSendPath = "/var/www/homeauto/smarthome/smartlights/codesend"
codeSendPin = "0"
codeSendPulseLength = "189"

lightsList = [
        {
		"lightId": "tubeLight",
		"name": "Living Room (Tube light)",
		"codes": {
                           "on": 1332995,
                           "off": 1333004
		}
	},
	{
		"lightId": "livingRoom",
		"name": "Living Room (Lamp)",
		"codes": {
                           "on": 1334531,
                           "off": 1334540
		}
	},
	{
		"lightId": "bedRoom",
		"name": "Bed Room",
		"codes": {
                           "on": 1340675,
                           "off": 1340684
		}
	}

]

class Ping(Resource):

        def __init__(self):
                super(Ping, self).__init__()

        def get(self):
                return "OK", 200

class LightList(Resource):

	def __init__(self):
		self.parser = reqparse.RequestParser()
		self.parser.add_argument('lightId', required=True, help="lightId is required!", location="json")
		self.parser.add_argument('name', required=True, help="name is required!", location="json")
		self.parser.add_argument('codes', required=True, location="json")
		super(LightList, self).__init__()

	def get(self):
		return {"lights": lightsList}, 200

	def post(self):
		args = self.parser.parse_args()
		print(args)

		light = {
			"lightId": args['lightId'],
			"name": args['name'],
			"codes": request.json['codes'] #args['codes']
		}

		lightsList.append(light)
		return {'light': light}, 201


class Light(Resource):

	def get(self, lightId):
		light = self.findLight(lightId)
		return light, 200

	def delete(self, lightId):
		isDeleted = False
		for light in lightsList:
			if light['lightId'] == lightId:
				lightsList.remove(light)
				isDeleted = True
				break

		#light = [light for light in jsonList if light['lightId'] == lightId]
		if isDeleted == True:
			return lightId + " deleted.", 200
		else:
			return "Light not deleted.", 404

	def put(self, lightId, action):

		if lightId.lower() == "all":
			for light in lightsList:
				if action.lower() == "on":
					code = self.getLightCode(light, action)
					self.triggerLightAction(code)
					
				elif action.lower() == "off":
					code = self.getLightCode(light, action)
					self.triggerLightAction(code)
				else:
					return 404
				
			return 200
		else:
		  
			light = self.findLight(lightId)

			if action.lower() == "on":
				code = self.getLightCode(light, action)
				self.triggerLightAction(code)
      
			elif action.lower() == "off":
				code = self.getLightCode(light, action)
				self.triggerLightAction(code)
      
			else:
				return 404

			return 200

	def triggerLightAction(self, lightCode):
		transmit = codeSendPath
		args = str(lightCode) + ' -p ' + codeSendPin + ' -l ' + codeSendPulseLength
		subprocess.call([transmit, args])
		time.sleep(1)
		return True
      
	def getLightCode(self, light, action):
		return light['codes'][action]
	  
	def findLight(self, lightId):
		#jsonList = json.loads(json.dumps(lightsList))
		light = next(item for item in lightsList if item['lightId'] == lightId)
		return light

#lightsapi.add_resource(LightList, "/api/v1/lights", endpoint="AllLights")
#lightsapi.add_resource(Light, "/api/v1/lights/<string:lightId>", endpoint="LightById")
#lightsapi.add_resource(Light, "/api/v1/lights/<string:lightId>/<string:action>", endpoint="TriggerLight")

#if __name__ == "__main__":
#  app.run(debug=True)
