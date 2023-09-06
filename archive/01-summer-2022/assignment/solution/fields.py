"""
This file details a list of fields to be web-scraped on the Talabat site.
We use pydantic (https://pydantic-docs.helpmanual.io/) to add types and validate fields. 
Pydantic is a python library that helps one to define data-models easily and JSONify the results.
While there are numerous libraries / frameworks or methods to validate types and data, we choose
Pydantic since it's easy to use, easy to understand and is battle-tested

Pydantic data models ensure that we only scrape the data using the types mentioned in README.md of
the assignment. This helps because:
1. When we upload the scraped data to a relational table, the column types can be matched to data model types
2. When we want to perform analysis on the scraped data, we spend less time on cleaning.

In the data-model, `restaurant_name` : str defines the field restaurant name and enforces it to be a string
Adding a `None` at the end ensures that the field can be nullable, as there may not be data about it
on the web page, and we still want the data to pass validation.
"""

from pydantic import BaseModel


class Talabat(BaseModel):
    # Talabat class "extends" BaseModel from pydantic to force type restrictions
    restaurant_name: str
    restaurant_logo: str = None
    latitude: float
    longitude: float
    cuisine_tags: list[str] = None

    # We define a separate model / class for menu items
    class TalabatMenuItem(BaseModel):
        item_name: str
        item_description: str = None
        item_price: float
        item_image: str = None

    # We define it as a list of a complex type (like structs in C, C++)
    menu_items: list[TalabatMenuItem]
