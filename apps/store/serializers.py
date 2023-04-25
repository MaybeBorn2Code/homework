# Python
from typing import Any

# DRF
from rest_framework import serializers

# Local
from .models import (
    Book,
    Author,
)


class BookSerializer(serializers.Serializer):
    """TeamLightSerializer."""

    title = serializers.CharField()
    pages = serializers.CharField()
    authors = serializers.PrimaryKeyRelatedField(
        queryset=Author.objects.all(), many=True)

    class Meta:
        model = Book
        fields = (
            'title',
            'pages',
            'authors'
        )
