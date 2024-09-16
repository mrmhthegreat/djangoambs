# import data to the database using command
from django.apps import apps
from typing import Any
from django.core.management.base import BaseCommand, CommandParser,CommandError
import csv


class Command(BaseCommand):
    help='import data to the database'
    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('file_path',type=str,help='path to the csv file ')
        parser.add_argument('model_name',type=str,help='Name of the app ')

    def handle(self, *args: Any, **options: Any) -> str | None:
        file_path=options['file_path']
        model_name=options['model_name'].capitalize()
        model=None
        for app_config in apps.get_app_configs():
            try:
                model=apps.get_model(app_config.label,model_name)
                break
            except LookupError:
                continue

        if not model:
            raise CommandError(f'Model {model_name} not found in any app')

        with open(file_path,'r') as file:
            reader=csv.DictReader(file)
            for row in reader:
                try:
                    model.objects.create(**row)
                except:
                    self.stdout.write(self.style.WARNING(f'Data "{row}" already Exit'))

        self.stdout.write(self.style.SUCCESS('Data Imported Successfully'))