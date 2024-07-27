from django.core.management.base import BaseCommand

from valuations.services.scraper import FullTitleScraper, SectionalTitleScraper


class Command(BaseCommand):
    help = 'Scrapes the Durban valuations website'

    def handle(self, *args, **options):
        FullTitleScraper().scrape()
        SectionalTitleScraper().scrape()

        self.stdout.write(self.style.SUCCESS('Successfully scraped the site!'))
