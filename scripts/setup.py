import pandas as pd
from astrodown import load_export

astrodown =  astrodown_js.to_py()
for export in astrodown["exports"]:
    globals()[export["name"]] = load_export(export)