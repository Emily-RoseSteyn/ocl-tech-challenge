import abc

import requests

from bs4 import BeautifulSoup

from src.valuations.services.get_valuation_suburbs import get_valuation_suburbs
from src.valuations.services.valuation_table_utils import save_table_data


class Scraper(metaclass=abc.ABCMeta):
    """Abstract class for scraping data from the valuations website"""

    # Could generalise even further by handling different websites but that's out of scope

    def __init__(self, roll_number):
        self._roll_number = roll_number

    def scrape(self):
        suburbs = get_valuation_suburbs()

        url = 'http://valuation2022.durban.gov.za/FramePages/SearchResult.aspx'

        # For each suburb, make request to get data
        for index, suburb in suburbs.iterrows():
            suburb_value = suburb["value"]
            search_url = (
                f"{url}?Roll={self._roll_number}&VolumeNo=&RateNumber=&StreetNo=&StreetName=&Suburb={suburb_value}"
                f"&ERF=&Portion=&DeedsTown=&SchemeName=&SectionNumber=&All=true")

            print(search_url)
            response = requests.get(search_url)
            soup = BeautifulSoup(response.content, 'html.parser')
            table = soup.find('table', class_='searchResultTable')

            if table:
                print("Table found")
                save_table_data(table)

            else:
                print("Table not found")

            # TODO: Remove break
            break


class FullTitleScraper(Scraper):
    """Scrapes the full titles from the valuations website"""

    def __init__(self):
        roll_number = 1
        super().__init__(roll_number)


class SectionalTitleScraper(Scraper):
    """Scrapes the sectional titles from the valuations website"""

    def __init__(self):
        roll_number = 2
        super().__init__(roll_number)

