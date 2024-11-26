import requests
from django.core.cache import cache


def get_valid_breeds() -> list[str]:
    cache_key = "valid_cat_breeds"
    breeds = cache.get(cache_key)

    if not breeds:
        response = requests.get("https://api.thecatapi.com/v1/breeds")
        if response.status_code == 200:
            data = response.json()
            breeds = [breed["name"] for breed in data]
            cache.set(cache_key, breeds, timeout=(60 * 60))  # Cache for 1 hour
        else:
            raise Exception(
                f"Failed to fetch breed data from TheCatAPI. "
                f"Error with code: {response.status_code}"
            )
    return breeds
