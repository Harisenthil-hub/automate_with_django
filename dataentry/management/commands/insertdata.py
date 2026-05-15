from django.core.management.base import BaseCommand
from dataentry.models import Student


class Command(BaseCommand):
    
    help = 'It will insert data to the database'
    
    def handle(self, *args, **kwargs):
        
        dataset = [
            { 'roll_no': 1002, 'name': 'Deepak', 'age': 22 },
            { 'roll_no': 1003, 'name': 'Logesh', 'age': 19 },
            { 'roll_no': 1004, 'name': 'Dharaneesh', 'age': 21 },
            { 'roll_no': 1005, 'name': 'Jai', 'age': 23 },
            { 'roll_no': 1006, 'name': 'Krishna', 'age': 24 },
        ]
        
        for data in dataset:
            
            if not Student.objects.filter(roll_no=data['roll_no']).exists():
                Student.objects.create(roll_no=data['roll_no'], name=data['name'], age=data['age'])
                
            else:
                self.stdout.write(
                    self.style.WARNING(f'Student with this roll no {data['roll_no']} already exists.')
                )
        
        self.stdout.write(
            self.style.SUCCESS('Data inserted successfully!')
        )
        