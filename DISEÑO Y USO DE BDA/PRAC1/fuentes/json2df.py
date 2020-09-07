import pandas as pd

import json

with open('COUNTRY.json') as f:
  data = json.load(f)

# Output: {'name': 'Bob', 'languages': ['English', 'Fench']}
x=pd.DataFrame(data)
print(x)