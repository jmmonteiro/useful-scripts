import click
import pandas as pd
from pandas.api.types import is_numeric_dtype


@click.command()
@click.option("-i", default="revolut.csv", help="input filename")
@click.option("-o", default="out.csv", help="output filename")
def convert(i, o):
    data = pd.read_csv(i, delimiter=";", decimal=",")
    data.columns = [
        "Completed Date",
        "Description",
        "Paid Out",
        "Paid In",
        "Exchange Out",
        "Exchange In",
        "Balance",
        "Category",
        "Notes",
    ]
    data["Completed Date"] = [
        x.replace(" ", "").replace(u"\u00A0", "") for x in data["Completed Date"]
    ]
    data["Completed Date"] = pd.to_datetime(data["Completed Date"], format="%d/%m/%Y")
    data["Description"] = [x.strip() for x in data["Description"]]
    data["Notes"] = [x.strip() for x in data["Notes"]]

    for c in ["Paid Out", "Paid In", "Balance"]:
        if not is_numeric_dtype(data[c]):
            data[c] = [x.replace(" ", "").replace(u"\u00A0", "") for x in data[c]]
            data[c] = [x if x != "" else "0,00" for x in data[c]]
            data[c] = pd.to_numeric(
                [x.replace(".", "").replace(",", ".") for x in data[c]]
            )

    data.to_csv(o, index=False)


if __name__ == "__main__":
    convert()  # pylint: disable=E1120
