# DRF
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

# Django
from django.shortcuts import render
from django.db.models.query import QuerySet

# Local
from .serializers import BookSerializer
from .models import Book
from abstracts.mixins import ResponseMixin, ObjectMixin


class MainViewSet(ResponseMixin, ObjectMixin, ViewSet):

    queryset = Book.objects.prefetch_related('authors')[:1000]

    def list(self, request: Request) -> Response:
        """GET method."""

        serializer: BookSerializer = \
            BookSerializer(
                self.queryset,
                many=True
            )
        return self.get_json_response(serializer.data, 'books')
