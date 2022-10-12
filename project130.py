import pandas as pd

data = pd.open_csv('prject119data.py')
del data['Luminosity']
print(data)

