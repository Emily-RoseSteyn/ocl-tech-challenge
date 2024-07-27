from datetime import datetime

import pandas as pd

from django.conf import settings
from sqlalchemy import create_engine

user = settings.DATABASES['default']['USER']
password = settings.DATABASES['default']['PASSWORD']
database_name = settings.DATABASES['default']['NAME']
host = settings.DATABASES['default']['HOST']
port = settings.DATABASES['default']['PORT']

database_url = f'postgresql+psycopg://{user}:{password}@{host}:{port}/{database_name}'
engine = create_engine(database_url, echo=False)


def process_cells(cells):
    row_data = []
    for cell in cells:
        row_data.append(cell.text.strip())
    return row_data


def save_table_data(table, roll_type):
    # Check if any data
    rows = table.find_all('tr', {'class': ['color0', 'color1']})

    if len(rows) == 0:
        print('No data')
        return

    # Get headers
    header_content = table.find_all('tr', class_='SearchResultRowHeader')
    # Assuming only one row of header content
    header_cells = header_content[0].find_all(['th', 'td'])
    headers = process_cells(header_cells)

    # Get data
    data = []

    for row in rows:
        cells = row.find_all(['th', 'td'])
        data.append(process_cells(cells))

    df = pd.DataFrame(data, columns=headers)

    if not df.empty:
        # Rename columns
        df = df.rename(columns={
            'Rate Number': 'rate_number',
            'Legal Description': 'legal_description',
            'Address': 'address',
            'First Owner': 'first_owner',
            'Use Code': 'use_code',
            'Rating Category': 'rating_category',
            'Market Value': 'market_value',
            'Registered Extent': 'registered_extent',
        })
        df["roll_type"] = roll_type

        # Index and order for consistency
        df.set_index('rate_number', inplace=True)
        df.sort_index(inplace=True)

        # Modify types
        df['market_value'] = df['market_value'].str.replace(',', '').replace('', '0').astype(float)
        df['registered_extent'] = df['registered_extent'].str.replace(',', '').replace('', '0').astype(float)

        # Save the data
        print(f'Saving {len(rows)} rows of data')
        df.to_sql('valuations_valuation', engine, if_exists='append', index=True)

    else:
        print('No data found')
