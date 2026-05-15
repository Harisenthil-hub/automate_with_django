from django.core.management.base import BaseCommand
from dataentry.models import Student
import csv


class Command(BaseCommand):
    help = 'Import data from csv file'
    
    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the csv file')
        
    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if not Student.objects.filter(roll_no=row['roll_no']).exists():
                   Student.objects.create(**row)
                else:
                    self.stdout.write(
                        self.style.WARNING(f'Student with this roll no {row['roll_no']} already exists.')
                    )
        
        self.stdout.write(self.style.SUCCESS('Data imported from CSV Successfully!'))