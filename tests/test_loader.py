exports = [
    {"name": "codes", "type": "pandas", "value": "https://media.githubusercontent.com/media/qiushiyan/blog-data/main/codes.csv"}
]

def test_pandas_csv():
    import pandas as pd
    from astrodown import load_export

    df = load_export(exports[0])
    assert isinstance(df, pd.DataFrame)