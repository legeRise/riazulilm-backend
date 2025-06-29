from django.core.management.base import BaseCommand
from books.models import Book
from faker import Faker
import random

class Command(BaseCommand):
    help = 'Seed the database with dummy Book data'

    def handle(self, *args, **kwargs):
        fake = Faker()
        for _ in range(20):  # Change 20 to any number of books you want
            Book.objects.create(
                title=fake.sentence(nb_words=4),
                description=fake.paragraph(),
                author=fake.name(),
                published_date=fake.date_between(start_date='-10y', end_date='today'),
                pages=random.randint(50, 1000),
                cover_image=fake.image_url(),
                download_url=fake.url(),
            )
        self.stdout.write(self.style.SUCCESS('Successfully seeded Book data'))
