from django.core.management.base import BaseCommand, CommandError
from nutriFood.models import Product
import requests

class Command(BaseCommand):
    openFoodFactUrl = 'https://world.openfoodfacts.org/api/v2/search?page_size=100&categories_tags_fr'

    def add_arguments(self, parser):
        parser.add_argument('categories', nargs='+', type=str)

    def handle(self, *args, **options):
        for num, category in enumerate(options["categories"], start=0):
            try:
                if num == 0:
                  self.openFoodFactUrl += '=' + category
                else:
                    self.openFoodFactUrl += ',' + category
            except Product.DoesNotExist:
                raise CommandError("Une erreur est survenue")
        response = requests.get(self.openFoodFactUrl)
        if response.status_code == 200:
            data = response.json()
            for product in data["products"]:
                ingredients = ''
                if "ingredients" in product:
                    for num, ingredient in enumerate(product["ingredients"], start=0):
                        if num == 0:
                            ingredients += ingredient["text"]
                        else:
                            ingredients += ', ' + ingredient["text"]
                    existingProducts = Product.objects.filter(name=product["product_name"], ingredient=ingredients)
                    if len(existingProducts) == 0:
                        Product.objects.create(ingredient=ingredients, name=product["product_name"])
                        self.stdout.write(self.style.SUCCESS("Création de " + product["product_name"]))
            self.stdout.write(self.style.SUCCESS("Toutes les données sont créées"))
        else:
            self.stdout.write(self.style.ERROR(response))