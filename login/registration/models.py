from mongoengine import *
from login.settings import MONGO_DATABASE_NAME
class loginn(Document):
    firstname = StringField(max_length=120, required=True)
    lastname = StringField(max_length=500, required=True)
    pwd = DateTimeField(required=True)

	