from pytest_pyodide import run_in_pyodide


exports = [
    {"name": "codes", "type": "pandas", "value": "https://media.githubusercontent.com/media/qiushiyan/blog-data/main/codes.csv"}
]

@run_in_pyodide(packages = ["pandas", "astrodown"])
def test_pandas_csv(selenium):
    import pandas as pd
    from astrodown import load_export

    df = load_export(exports[0])
    assert isinstance(df, pd.DataFrame)