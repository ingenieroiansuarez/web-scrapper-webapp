import requests
import selectorlib

from datetime import datetime

URL = "https://programmer100.pythonanywhere.com"

def scrape(URL):
    """Scrape the tour data from the given URL."""
    response = requests.get(URL)
    source = response.text
    return source

def extract(source):

    extractor = selectorlib.Extractor.from_yaml_file("extract1.yaml")
    value = extractor.extract(source)["temp"]
    return value


def store(extracted):
    """Store the extracted data in a file."""
    with open("data.txt", "a") as file:
        file.write(extracted + "\n")

def read(extracted):
    """Read the extracted data from the file."""
    with open("data.txt", "r") as file:
        return file.read()

if __name__ == "__main__":
    # Scrape the data
    scraped = scrape(URL)
    extracted = extract(scraped)
    print(extracted)

    content = read(extracted)

