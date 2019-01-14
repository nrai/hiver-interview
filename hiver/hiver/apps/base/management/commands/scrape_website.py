from django.core.management import BaseCommand
from hiver.apps.base.services.scrape_hiver import find_commonly_used_words
import logging

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    """
    Base Command
    """

    help = "Calculate distance of the product id given"

    def handle(self, *args, **options):
        """

        :param args:
        :param options:
        :return:
        """

        find_commonly_used_words()
