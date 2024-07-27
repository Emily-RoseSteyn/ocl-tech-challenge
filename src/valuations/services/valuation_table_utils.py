import pandas as pd


def process_cells(cells):
    row_data = []
    for cell in cells:
        row_data.append(cell.text.strip())
    return row_data


def save_table_data(table):
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
    print('Saving data')
    print(df)
    # TODO: Actually save the data
