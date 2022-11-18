from parser import parse as talabat_parse
import pandas as pd
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm as tqdm_pandas

tqdm_pandas.pandas()


def main():
    # read sample data from JSON into pandas dataframe
    url_df: pd.DataFrame = pd.read_json("data/sample.json")
    url_df.columns = ["url"]

    # Fetch data, convert it to beautiful soup and parse it using parse function
    url_df["response"] = url_df["url"].progress_apply(requests.get)
    url_df["soup_object"] = url_df["response"].apply(
        lambda response: BeautifulSoup(response.text, "lxml")
    )
    url_df["talabat_data"] = url_df["soup_object"].apply(talabat_parse)
    url_df["talabat_dict"] = url_df["talabat_data"].apply(lambda data: data.dict())

    # Create a dataframe / table from the parsed data
    talabat_df: pd.DataFrame = pd.json_normalize(url_df["talabat_dict"])

    # Write to file
    talabat_df.to_parquet("data/talabat_restaurant_data.parquet", index=False)


if __name__ == "__main__":
    main()