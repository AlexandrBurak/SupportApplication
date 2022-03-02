from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from tickets.models import Ticket, Feedback, Support

from django.contrib.auth.models import User
from rest_framework.test import APIClient, APITestCase, force_authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from django.urls import reverse

from http import HTTPStatus

User = get_user_model()


class TicketsURLTests(APITestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create(username='user')
        cls.sup = User.objects.create(username='Open')
        cls.supp = Support.objects.create(supporter=cls.sup)

    def setUp(self):
        user = TicketsURLTests.user
        sup = TicketsURLTests.sup
        self.authorized_user = APIClient()
        self.authorized_sup = APIClient()
        self.authorized_user.credentials(HTTP_AUTHORIZATION=
                                         f'Bearer '
                                         f'{RefreshToken.for_user(user).access_token}')
        self.authorized_sup.credentials(HTTP_AUTHORIZATION=
                                        f'Bearer '
                                        f'{RefreshToken.for_user(sup).access_token}')

    def test_ticket_create(self):
        self.assertFalse(Ticket.objects.filter(text='New ticket!').exists())
        self.authorized_user.post(reverse('tickets-list'), {'text': 'New ticket!'})
        self.assertTrue(Ticket.objects.filter(text='New ticket!').exists())

