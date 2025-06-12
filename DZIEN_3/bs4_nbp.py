import requests
from bs4 import BeautifulSoup


def fetch_exchange_rates():
    try:
        url = "https://nbp.pl/statystyka-i-sprawozdawczosc/kursy/tabela-a/"
        response = requests.get(url)

        if response.status_code != 200:
            print(f"Błąd podczas pobierania danych. Kod statusu: {response.status_code}")
            return

        response.encoding = "windows-1250"
        soup = BeautifulSoup(response.text, "html.parser")

        # Bardziej precyzyjny selektor - szukamy tabeli w konkretnym miejscu
        table = soup.find_all("table", {"class": "table table-striped table-bordered table-hover table-sm"})
        # table = soup.find(
        #     "table", {"class": "table table-striped table-bordered table-hover table-sm"}
        #

        if not table:
            print("Nie znaleziono tabeli z kursami walut.")
            return

        print(f"KURSY WALUT (Tabela A - NBP):\n")
        rows = table.find_all("tr")[2:]

        for row in rows:
            cols = row.find_all("td")
            if len(cols) == 3:
                currency_name = cols[0].text.strip()
                currency_code = cols[1].text.strip()
                currency_rate = cols[2].text.strip()
                print(f"{currency_name} ({currency_code}): {currency_rate} PLN")

    except requests.RequestException as e:
        print(f"Wystąpił błąd podczas połączenia: {e}")
    except Exception as e:
        print(f"Wystąpił nieoczekiwany błąd: {e}")


fetch_exchange_rates()
