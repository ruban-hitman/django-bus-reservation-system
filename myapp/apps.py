#from django.apps import AppConfig


#class MyappConfig(AppConfig):
    #pname = 'myapp'
# In your myapp/apps.py
from django.apps import AppConfig

class MyappConfig(AppConfig):
    name = 'myapp'
    default_auto_field = 'django.db.models.BigAutoField'
