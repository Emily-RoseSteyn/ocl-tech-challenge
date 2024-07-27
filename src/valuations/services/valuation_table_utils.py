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
    data = []
    headers = []

    # Skip the first row which has the number of results
    rows = table.find_all('tr')[1:]

    for row in rows:
        cells = row.find_all(['th', 'td'])
        if not headers:
            headers = process_cells(cells)
        else:
            data.append(process_cells(cells))

    df = pd.DataFrame(data, columns=headers)

    if not df.empty:
        print('Saving data')
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

        # TODO: Actually save the data
        print(df)
        df.to_sql('valuations_valuation', engine, if_exists='append', index=False)

    else:
        print('No data found')
