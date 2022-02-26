from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import FeedbackViewSet, TicketSupportViewSet, TicketViewSet

router = SimpleRouter()

router.register(r'supporter/tickets', TicketSupportViewSet, basename='sups_ticks')
router.register(r'supporter/tickets/(?P<ticket_id>\d+)/feedbacks',
                FeedbackViewSet, basename='feedbacks_sup')
router.register(r'tickets', TicketViewSet, basename='tickets')
router.register(r'tickets/(?P<ticket_id>\d+)/feedbacks',
                FeedbackViewSet, basename='feedbacks_usr')
urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
