import os
import sys

#Virtual env settings
activate_this = '/var/www/homeauto/venv_python3.4/bin/activate_this.py'

#Commenting below since it is not supported for 3.4
#execfile(activate_this, dict(__file__=activate_this))

exec(compile(open(activate_this, "rb").read(), activate_this, 'exec'), dict(__file__=activate_this))

#Replace standard out
sys.stdout = sys.stderr

#Add this file path to sys.path in order to import settings
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)),'../..'))

#Add this file path to sys.path in order to import app
sys.path.append('/var/www/smarthome/')

#Create application for our app
from runapp import app as application
