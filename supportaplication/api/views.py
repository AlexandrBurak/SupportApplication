from django.db.models import Count
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated

from api.permissions import IsReadOnly, IsSupporter
from api.serializers import FeedbackSerializer, TicketSerializer
from tickets.models import Support, Ticket


class TicketSupportViewSet(viewsets.ModelViewSet):
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated, IsSupporter]

    def get_queryset(self):
        return self.request.user.support.tickets

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)


class TicketViewSet(viewsets.ModelViewSet):
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated, IsReadOnly]

    def perform_create(self, serializer):
        supporter = get_object_or_404(Support,
                                      pk=Support.objects.
                                      annotate(count_ticks=
                                               Count('tickets')).
                                      order_by('count_ticks')[0])
        serializer.save(author=self.request.user, supporter=supporter,
                        text=self.request.data.get('text'))

    def get_queryset(self):
        return self.request.user.tickets


class FeedbackViewSet(viewsets.ModelViewSet):
    serializer_class = FeedbackSerializer
    permission_classes = [IsAuthenticated, IsReadOnly]

    def perform_create(self, serializer):
        ticket = get_object_or_404(Ticket,
                                   pk=self.kwargs.get('ticket_id'))
        serializer.save(sender=self.request.user, ticket=ticket)

    def get_queryset(self):
        ticket = get_object_or_404(Ticket,
                                   pk=self.kwargs.get('ticket_id'))
        return ticket.feedbacks.order_by('departure_date')
