from typing import Any
from django.core.management.base import BaseCommand, CommandParser

class Command(BaseCommand):
    help='Greet'
    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('name',type=str,help='Name For ')

        pass
    def handle(self, *args: Any, **options: Any) -> str | None:
        name=options['name']
        self.stdout.write(f'hi {name}')