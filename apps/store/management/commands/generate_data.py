# Python
import random
from typing import Any
from datetime import datetime

# Django
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

# Local
from store.models import Book, Author


class Command(BaseCommand):
    """Custom command for filling up database."""

    help = 'Custom command for filling up database'

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super(Command, self).__init__(*args, **kwargs)
        # pass

    def generate_data(self) -> None:
        for i in range(1000):
            user = User.objects.create_user(
                username=f'user_{i}', password='password')
            Author.objects.create(user=user, sm_pp=random.randint(1, 5))
            num_pages = random.randint(50, 1000)
            num_authors = random.randint(1, 5)
            book = Book.objects.create(title=f'Book {i}', pages=num_pages)
            # Selecting random Authors and adding to the book
            authors = Author.objects.order_by('?')[:num_authors]
            book.authors.set(authors)

        print('data_generated!')

    def handle(self, *args: Any, **kwargs: Any) -> None:
        self.generate_data()
