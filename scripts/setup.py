import astrodown.js

# astrodown_js is passed through javascript using pyodide.globals.set("astrodown_js", value)
def set_global(name: str, value: str):
    astrodown.globals[name] = value


[
    set_global(export["name"], astrodown.js.load_export(export))
    for export in astrodown_js["exports"]
]
