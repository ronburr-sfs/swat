from django.core.management.base import BaseCommand, CommandError
from items.models import Item


class Command(BaseCommand):
    help = "Imports text below."

    items = [
        'Chest press 50',
        'Overhead press 30',
        'Chest wing 70',
        'Bicep 80',
        'Tricep 90',
        'Lat pull 115',
        'Abs 1 160',
        'Back 160',
        'Leg press 130',
        'Leg lift 130',
        'Abs 2 80',
        'Leg extension 120',
        'Torso twist 130',
        'Cardio 3.7 @ 6 incline for 20 min',
    ]

    def add_arguments(self, parser):
        parser.add_argument("list_id", nargs="+", type=int)

    def handle(self, *args, **options):
        list_id = options['list_id'][0]
        for item_title in self.items:
            try:
                item = Item()
                item.list_id = list_id
                item.title = item_title
                item.status_id = 1
                item.save()
            except Item.DoesNotExist:
                raise CommandError('Unable to create item record.')

            self.stdout.write(
                self.style.SUCCESS('Successfully added item to list: ' + str(list_id))
            )