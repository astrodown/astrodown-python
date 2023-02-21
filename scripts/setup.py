from astrodown.js import load_export
from astrodown.utils import get_doc, inspect_function

astrodown = astrodown_js.to_py()
for export in astrodown["exports"]:
    globals()[export["name"]] = load_export(export)
