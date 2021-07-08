import os

MAPBOX_API_KEY = os.getenv('MAPBOX_API_KEY', '')
SQLALCHEMY_DATABASE_URI = 'sqlite:////var/lib/superset/superset.db'
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = 'thisISaSECRET_1234'
