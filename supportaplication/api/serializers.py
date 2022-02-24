from tickets.models import Ticket
from rest_framework import serializers


class TicketSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(read_only=True,
                                          slug_field='username')

    supporter = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Ticket
        fields = ('text', 'created_date', 'author', 'status', 'supporter')


