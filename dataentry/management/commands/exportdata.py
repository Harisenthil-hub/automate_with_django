from django.core.management.base import BaseCommand, CommandError
from django.apps import apps
import csv
from datetime import datetime

# desired command = python manage.py exportdata model_name
class Command(BaseCommand):
    help = 'Export data from student table to CSV file'
    
    def add_arguments(self, parser):
        parser.add_argument('model_name', type=str, help='Modal name')
    
    
    def handle(self, *args, **kwargs):
        
        model_name = kwargs['model_name'].capitalize()
        
        model = None
        for app_config in apps.get_app_configs():
            
            try:
                model = apps.get_model(app_config.label, model_name)
                break
            except LookupError:
                continue
            
        if not model:
            raise CommandError(f'Modal {model_name} could not be found')
        
        data = model.objects.all()
        
        timestamp = datetime.now().strftime('%Y-%m-%d,%H-%M-%S')
        file_path = f'exported_{model_name}_data_{timestamp}.csv'
       
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            
            writer.writerow([field.name for field in model._meta.fields])
            for dt in data:
                writer.writerow([getattr(dt, field.name) for field in model._meta.fields ])
                
        self.stdout.write(
            self.style.SUCCESS('Data exported successfully!')
        )
           
           
       