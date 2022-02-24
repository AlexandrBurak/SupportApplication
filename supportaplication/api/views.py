from api.serializers import TicketSerializer
from api.permissions import IsOwnerOrReadOnly
from tickets.models import Ticket, Support

from django.db.models import Count

from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        supporter = get_object_or_404(Support,
                                      pk=Support.objects.
                                      annotate(count_ticks=
                                               Count('tickets')).
                                      order_by('count_ticks')[0])
        serializer.save(author=self.request.user, supporter=supporter)
