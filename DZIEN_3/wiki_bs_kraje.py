import requests
from bs4 import BeautifulSoup

def fetch_country_capitals():
    url = "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_and_their_capitals_in_native_languages"
    response = requests.get(url)

    if response.status_code != 200:
        print("Failed to fetch the page")
        return

    soup = BeautifulSoup(response.text, "html.parser")

    # Znajdź pierwszą dużą tabelę z danymi
    table = soup.find("table", {"class": "wikitable"})

    if not table:
        print("No table found.")
        return

    print("Lista państw i ich stolic:\n")

    rows = table.find_all("tr")[1:]  # pomijamy nagłówek tabeli

    for row in rows[:20]:  # tylko 20 pierwszych dla przykładu
        cols = row.find_all("td")
        if len(cols) >= 2:
            country = cols[0].text.strip()
            capital = cols[1].text.strip()
            print(f"{country} — {capital}")

if __name__ == "__main__":
    fetch_country_capitals()
