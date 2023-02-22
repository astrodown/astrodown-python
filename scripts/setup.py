import astrodown.js


astrodown = astrodown_js.to_py()
for export in astrodown["exports"]:
    globals()[export["name"]] = astrodown.js.load_export(export)

# # astrodown_js is passed through javascript using pyodide.globals.set("astrodown_js", value)
# astrodown_js = astrodown_js.to_py()


# def _set_global(name: str, value: any):
#     globals()[name] = value


# [
#     _set_global(export["name"], astrodown.js.load_export(export))
#     for export in astrodown_js["exports"]
# ]
