from django.core.management.base import BaseCommand, CommandError
from nutriFood.models import Product

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('categories', nargs='+', type=str)

    def handle(self, *args, **options):
        for category in options["categories"]:
            try:
                self.stdout.write(self.style.SUCCESS(category))
            except Product.DoesNotExist:
                raise CommandError("Une erreur est survenue")
        self.stdout.write(self.style.SUCCESS('Successfully closed poll "%s"'))