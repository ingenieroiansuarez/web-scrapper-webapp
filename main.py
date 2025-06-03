# This script captures video from the webcam, detects motion, and sends an email alert when motion is detected.
import requests
import selectorlib

from datetime import datetime

# This script scrapes a webpage for tour data, extracts the relevant information, and stores it in a text file with a timestamp.
URL = "http://programmer100.pythonanywhere.com/"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
# # The URL to scrape for tour data
def scrape(url):
    """Scrape the page source from the URL"""
    response = requests.get(url, headers=HEADERS)
    source = response.text
    return source

# This function extracts the tour data from the scraped HTML source using selectorlib.
def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)["tours"]
    return value

# This function stores the extracted data in a text file with a timestamp.
def store(extracted):
    now = datetime.now().strftime("%y-%m-%d-%H-%M-%S")
    with open("data.txt", "a") as file:
        line = f"{now},{extracted}\n"
        file.write(line)


if __name__ == "__main__":
    scraped = scrape(URL)
    extracted = extract(scraped)
    print(extracted)
    store(extracted)
