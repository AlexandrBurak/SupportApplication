from supportaplication.settings import EMAIL_HOST_USER
from supportaplication.celery import app
from django.core.mail import send_mail


@app.task
def send_task(email):
    send_mail(
        subject='My API',
        message='Появился новый feedback',
        from_email=EMAIL_HOST_USER,
        recipient_list=[email],
        fail_silently=False
    )
