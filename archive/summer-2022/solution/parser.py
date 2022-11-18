"""
This file takes in the response as a beautifulsoup object of the web-page
and parses out individual elements with their respective types. It uses
the pydantic model from the `fields` module to reference the types and uses
the `get_next_data` function to get the data from the next.js response. 
This is then parsed directly instead of using HTML parsing (which is a bit less robust)
"""

from bs4 import BeautifulSoup
from fields import Talabat
from utils import get_next_data


def parse(soup: BeautifulSoup) -> Talabat:
    """A generic parse function for talabat that takes in the BeautifulSoup
    object of the web-page response and returns a parsed data object of type Talabat

    Args: soup (BeautifulSoup): The BeautifulSoup object of the web-page response
    Returns: Talabat: The parsed data object of type Talabat with all attributes embedded
    """
    nextjs_data: dict = get_next_data(soup)
    latitude, longitude = parse_center(nextjs_data)

    return Talabat(
        restaurant_name=parse_restaurant_name(nextjs_data),
        restaurant_logo=parse_restaurant_logo(nextjs_data),
        latitude=latitude,
        longitude=longitude,
        cuisine_tags=parse_cuisine_tags(nextjs_data),
        menu_items=parse_menu(nextjs_data),
    )


def parse_center(next_data: dict) -> tuple[float, float]:
    """A function that parses the center coordinates of the restaurant from the
    next.js response

    Args: next_data (dict): The next.js response as a dictionary
    Returns: tuple[float, float]: The latitude and longitude of the restaurant
    """
    coordinates_key = (
        next_data["props"]["pageProps"]["gtmEventData"]["restaurant"]
        if next_data["props"]["pageProps"]["gtmEventData"].get("restaurant")
        else next_data["props"]["pageProps"]["initialMenuState"]["restaurantObj"]
    )
    return [float(coordinates_key["latitude"]), float(coordinates_key["longitude"])]


def parse_restaurant_name(next_data: dict) -> str:
    """A function that parses the restaurant name from the next.js response

    Args: next_data (dict): The next.js response as a dictionary
    Returns: str: The restaurant name
    """
    brand_name = (
        next_data["props"]["pageProps"]["gtmEventData"]["restaurant"]["name"]
        if next_data["props"]["pageProps"]["gtmEventData"].get("restaurant")
        else next_data["props"]["pageProps"]["initialMenuState"]["restaurantObj"][
            "name"
        ]
    )
    return brand_name


def parse_restaurant_logo(next_data: dict) -> str:
    """A function that parses the restaurant logo from the next.js response

    Args: next_data (dict): The next.js response as a dictionary
    Returns: str: The restaurant logo as a URL text
    """
    logo = (
        next_data["props"]["pageProps"]["gtmEventData"]["restaurant"]["logo"]
        if next_data["props"]["pageProps"]["gtmEventData"].get("restaurant")
        else next_data["props"]["pageProps"]["initialMenuState"]["restaurantObj"][
            "logo"
        ]
    )
    return logo


def parse_cuisine_tags(next_data: dict) -> list[str]:
    """A function that parses the cuisine tags from the next.js response

    Args: next_data (dict): The next.js response as a dictionary
    Returns: list[str]: The cuisine tags as a list (array) of strings
    """
    cuisine_str = (
        next_data["props"]["pageProps"]["gtmEventData"]["restaurant"]["cuisineString"]
        if next_data["props"]["pageProps"]["gtmEventData"].get("restaurant")
        else next_data["props"]["pageProps"]["initialMenuState"]["restaurantObj"][
            "cuisineString"
        ]
    )
    return [cuisine.strip() for cuisine in cuisine_str.split(",")]


def parse_menu(next_data: dict) -> list[Talabat.TalabatMenuItem]:
    """A function that parses the menu from the next.js response

    Args: next_data (dict): The next.js response as a dictionary
    Returns: list[Talabat.TalabatMenuItem]: The menu as a list (array) of menu items
    """

    try:
        items = next_data.get("props").get("pageProps")["initialMenuState"]["menuData"][
            "items"
        ]
        return [
            Talabat.TalabatMenuItem(
                item_name=item.get("name"),
                item_description=item.get("description"),
                item_price=item.get("price"),
                item_image=item.get("image"),
            )
            for item in items
        ]
    except Exception as e:
        return []
