from django.contrib.auth import get_user_model
from django.test import TestCase

from ..models import Ticket, Support, Feedback

User = get_user_model()


class TicketsModelTests(TestCase):
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

    def test_models_have_correct_object_names(self):
        """Проверяем, что у моделей корректно работает __str__."""
        ticket = TicketsModelTests.ticket
        feedback = TicketsModelTests.feedback
        models_for_test = [ticket, feedback, ticket.supporter]
        for model in models_for_test:
            with self.subTest(model=model):
                self.assertEqual(str(model), 'Open')
