from io import StringIO

import pandas as pd
import requests

from bs4 import BeautifulSoup


def get_suburbs():
    url = 'http://valuation2022.durban.gov.za/FramePages/SearchCrit.aspx'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the select tag by ID (optional)
    select_tag = soup.find('select', id='drpSuburb')

    # Find all option tags within the select tag
    options = select_tag.find_all('option')

    # Extract text and value for each option
    option_data = []
    for option in options:
        text = option.text.strip()
        value = option.get('value')

        if value:
            option_data.append({'text': text, 'value': value})

    return pd.DataFrame(option_data)


def scrape_full_title():
    suburbs = get_suburbs()

    url = 'http://valuation2022.durban.gov.za/FramePages/Search.aspx'

    # For each suburb, make request to get data
    for index, suburb in suburbs.iterrows():
        suburb_value = suburb["value"]
        search_url = (f"{url}?Roll=1&VolumeNo=&RateNumber=&StreetNo=&StreetName=&Suburb={suburb_value}"
                      f"&ERF=&Portion=&DeedsTown=&SchemeName=&SectionNumber=&All=false")

        print(search_url)
        response = requests.get(search_url)
        soup = BeautifulSoup(response.content, 'html.parser')
        print(soup)
        break

scrape_full_title()
# Full title
# "https://valuation2022.durban.gov.za/FramePages/SearchResult.aspx?Roll=1&VolumeNo=&RateNumber=&StreetNo=&StreetName=&Suburb=22136&ERF=&Portion=&DeedsTown=&SchemeName=&SectionNumber=&All=false"
# Sectional title
# "https://valuation2022.durban.gov.za/FramePages/SearchResult.aspx?Roll=2&VolumeNo=&RateNumber=&StreetNo=&StreetName=&Suburb=22136&ERF=&Portion=&DeedsTown=&SchemeName=&SectionNumber=&All=false"
