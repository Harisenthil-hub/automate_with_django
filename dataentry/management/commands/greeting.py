from django.core.management.base import BaseCommand


class Command(BaseCommand):
    
    help = 'Greets the user'
    
    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Specifies the user name')
    
    def handle(self, *args, **kwargs):
        
        name = kwargs['name']
        greeting = f'Hi {name}, Good morning!'
        self.stdout.write(greeting)
        
    
        