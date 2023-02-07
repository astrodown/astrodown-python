from astrodown import load_export
import sys


astrodown =  astrodown_js.to_py()
for export in astrodown["exports"]:
    globals()[export["name"]] = load_export(export)