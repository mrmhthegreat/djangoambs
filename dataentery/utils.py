# import data to the database using command
from django.apps import apps
def get_all_custom_model()-> list|None:
    defualt_model=['LogEntry', 'Permission', 'Group', 'User', 'ContentType', 'Session']
    custom_model=[]
    for model in apps.get_models():
        if model.__name__ not in defualt_model:
            custom_model.append(model.__name__)
    return custom_model
 
