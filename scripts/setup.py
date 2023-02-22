import astrodown.js


astrodown_js = astrodown_js.to_py()
print(astrodown_js)
# for export in astrodown_js["exports"]:
#     print(export, astrodown.js.load_export(export))
#     globals()[export["name"]] = astrodown.js.load_export(export)

# # astrodown_js is passed through javascript using pyodide.globals.set("astrodown_js", value)
# astrodown_js = astrodown_js.to_py()


# def _set_global(name: str, value: any):
#     globals()[name] = value


# [
#     _set_global(export["name"], astrodown.js.load_export(export))
#     for export in astrodown_js["exports"]
# ]
