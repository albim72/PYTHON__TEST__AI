import requests
import time


def check_website_status(url):
    start_time = time.time()
    response = requests.get(url)
    elapsed = time.time() - start_time

    print(f"URL: {url} | Status: {response.status_code} | Time: {elapsed}")

check_website_status("https://www.gov.pl/web/gov")
