from django.apps import apps

def get_all_custom_models():
    
    default_models = ['User', 'LogEntry', 'Permission', 'Group', 'ContentType', 'Session', 'Upload']
    
    custom_models = []
    
    for models in apps.get_models():
        if models.__name__ not in default_models:
            custom_models.append(models.__name__)
        
    return custom_models