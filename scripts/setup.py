import pandas as pd
from astrodown import load_export
from pyodide.http import open_url

astrodown =  astrodown_js.to_py()
for export in astrodown:
    globals()[export["name"]] = load_export(export)