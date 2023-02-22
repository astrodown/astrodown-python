import astrodown

# astrodown_js is passed through javascript using pyodide.globals.set("astrodown_js", value)
astrodown = astrodown_js.to_py()
for export in astrodown["exports"]:
    globals()[export["name"]] = astrodown.js.load_export(export)
