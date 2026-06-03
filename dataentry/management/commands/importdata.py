from django.core.management.base import BaseCommand, CommandError
# from dataentry.models import Student
from django.apps import apps
from django.db import DataError
import csv
from dataentry.utils import check_csv_errors

# Proposed Command - python manage.py importdata file_path model_name
class Command(BaseCommand):
    help = 'Import data from csv file'
    
    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the csv file')
        parser.add_argument('model_name', type=str, help='Name of the model')
        
    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        model_name = kwargs['model_name'].capitalize()
        
        model = check_csv_errors(file_path, model_name)
        
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                model.objects.create(**row)
        
        self.stdout.write(self.style.SUCCESS('Data imported from CSV Successfully!'))