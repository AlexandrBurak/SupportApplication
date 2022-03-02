from django.contrib.auth import get_user_model
from django.db import models
from django.core.exceptions import ValidationError

User = get_user_model()

CHOISES = (
    ('Open', 'Open'),
    ('Close', 'Close'),
    ('Freeze', 'Freeze'),
)


class Support(models.Model):
    supporter = models.OneToOneField(User,
                                     on_delete=models.CASCADE,
                                     primary_key=True,
                                     related_name='support',
                                     default=None)

    def __str__(self):
        return self.supporter.username


class Ticket(models.Model):
    text = models.TextField()
    created_date = models.DateField(
        'Дата создания', auto_now_add=True
    )
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='tickets')

    supporter = models.ForeignKey(Support,
                                  on_delete=models.SET_NULL,
                                  related_name='tickets',
                                  blank=True,
                                  null=True)

    status = models.CharField(max_length=50, choices=CHOISES,
                              default='Open')

    def __str__(self):
        return self.status


class Feedback(models.Model):
    ticket = models.ForeignKey(Ticket,
                               on_delete=models.CASCADE,
                               related_name='feedbacks',)
    message = models.TextField()
    departure_date = models.DateField(
        'Дата отправки', auto_now_add=True)
    sender = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='feedbacks')

    def __str__(self):
        return self.message
