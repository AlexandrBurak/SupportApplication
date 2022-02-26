from rest_framework import serializers

from tickets.models import Feedback, Ticket


class TicketSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(read_only=True,
                                          slug_field='username')

    supporter = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Ticket
        fields = ('pk', 'text', 'created_date', 'author', 'status', 'supporter')
        read_only_fields = ('pk', 'text', 'created_date', 'author', 'supporter')


class FeedbackSerializer(serializers.ModelSerializer):
    ticket = serializers.PrimaryKeyRelatedField(read_only=True)
    sender = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Feedback
        fields = ('ticket', 'message', 'sender', 'departure_date')
