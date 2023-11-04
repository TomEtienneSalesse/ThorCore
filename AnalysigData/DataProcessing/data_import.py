import pandas as pd

def import_data(file_path):
    data = pd.read_excel(file_path, header=None)
    return data
