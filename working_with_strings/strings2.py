import pandas as pd
import numpy as np

s = pd.Series(['foo', 'bar', 'faa', 'baa', np.nan])
s = s.str.replace('r$', 'gaa', regex=True)
print(s)