import astrodown.js


astrodown_js = astrodown_js.to_py()
# astrodown_js is passed through javascript using pyodide.globals.set("astrodown_js", value)
def _set_global(name: str, value: str):
    astrodown.globals[name] = value


[
    _set_global(export["name"], astrodown.js.load_export(export))
    for export in astrodown_js["exports"]
]
