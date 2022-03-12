from supportaplication.celery import app
from django.core.mail import send_mail


@app.task
def del_close_ticket(email):
    send_mail(
        subject='My API',
        message='Появился новый feedback',
        from_email='axndrspamacc@gmail.com',
        recipient_list=['buraksash@gmail.com', ],
        fail_silently=False
    )
