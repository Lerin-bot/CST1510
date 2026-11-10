# Fixed version.
# This was intentionally broken to practise debugging.

import pandas as pd

df = pd.DataFrame({
    "label": ["R-001", "R-002", "R-003"],
    "value": [87, 120, 45],
    "limit": [100, 100, 100],
})

print(df)
