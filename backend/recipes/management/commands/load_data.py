import json

from django.core.management.base import BaseCommand

from foodgram import settings
from django.apps import apps

Ingredient = apps.get_model('recipes', 'Ingredient')
Tag = apps.get_model('recipes', 'Tag')


class Command(BaseCommand):
    help = ' Загрузить данные в модель ингредиентов '

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING('Старт команды'))
        with open(f'{settings.BASE_DIR}/data/ingredients.json', encoding='utf-8',
                  ) as data_file_ingredients:
            ingredient_data = json.loads(data_file_ingredients.read())
            for ingredients in ingredient_data:
                Ingredient.objects.get_or_create(**ingredients)

        self.stdout.write(self.style.SUCCESS('Данные загружены'))
