"""Convert USD to ZAR."""

import typer


if __name__ == "__main__":
    import currency
    typer.run(currency.convert)