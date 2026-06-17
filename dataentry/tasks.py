from celery import shared_task
from django.core.management import call_command
import time
from django.core.mail import EmailMessage
from django.conf import settings
from .utils import send_email_notification, generate_csv_file


@shared_task
def celery_test_task():
    time.sleep(10)
    
    # sending Email
    mail_subject = 'Test subject'
    message = 'This is test email'
    to_email = settings.DEFAULT_TO_EMAIL
    send_email_notification(mail_subject, message, [to_email])
    return "Email sent successfully"


@shared_task
def import_data_task(full_path, model_name):
    try:
        call_command('importdata',full_path,model_name)
    except Exception as e:
        raise e
    
    mail_subject = 'Import Data Completed'
    message = 'Your data import has been successfull'
    to_email = settings.DEFAULT_TO_EMAIL
    send_email_notification(mail_subject, message, [to_email])
    return "Data imported succesfully"


@shared_task
def export_data_task(model_name):
    try:
        call_command('exportdata', model_name)
    except Exception as e:
        raise e
    
    file_path = generate_csv_file(model_name)
    
    mail_subject = 'Export Data Successful'
    message = 'Export data successfull. Please find the attachment'
    to_email = settings.DEFAULT_TO_EMAIL
    send_email_notification(mail_subject, message, [to_email], attachment=file_path)
    return "Export data task executed  succesfully"