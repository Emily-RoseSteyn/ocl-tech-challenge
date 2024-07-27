import pandas as pd
import requests
from bs4 import BeautifulSoup


def get_valuation_suburbs():
    # Noted that this URL does change to SearchCrit2 for sectional title
    # But assuming suburbs are the same for both full title and sectional title
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
