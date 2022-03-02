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
        cls.ticket = Ticket.objects.create(
            text='Help me!',
            author=cls.user,
            supporter=cls.supp,
            status='Open'
        )
        cls.feedback = Feedback.objects.create(
            message='Open',
            ticket=cls.ticket,
            sender=cls.user
        )

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

    def test_urls_auth(self):
        """Проверяем доступность для пользователя"""
        url_names = [
            '/api/tickets/',
            f'/api/tickets/{TicketsURLTests.ticket.pk}/',
            f'/api/tickets/{TicketsURLTests.ticket.pk}/feedbacks/',
        ]
        for address in url_names:
            with self.subTest(address=address):
                response = self.authorized_user.get(address)
                self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_urls_sup(self):
        """Проверяем доступность для саппортера"""
        url_names = [
            '/api/supporter/tickets/',
            f'/api/supporter/tickets/{TicketsURLTests.ticket.pk}/',
            f'/api/supporter/tickets/{TicketsURLTests.ticket.pk}/feedbacks/',
        ]
        for address in url_names:
            with self.subTest(address=address):
                response = self.authorized_sup.get(address)
                self.assertEqual(response.status_code, HTTPStatus.OK)
