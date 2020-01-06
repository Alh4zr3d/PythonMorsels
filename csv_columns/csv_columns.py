import csv

def csv_columns(fileObj, *, headers=None, missing=None):
    r = csv.reader(fileObj)
    if headers is None:
        headers = next(r)
    cols = {header: [] for header in headers}
    for row in r:
        for i, header in enumerate(headers):
            try:
                cols[header].append(row[i])
            except IndexError:
                cols[header].append(missing)
    return cols
