from playwright.sync_api import sync_playwright, expect


def allegro_search():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # zmiana na False dla lepszego debugowania
        page = browser.new_page()

        # Dodanie timeoutu dla nawigacji
        page.goto("https://allegro.pl", wait_until="networkidle")

        # Akceptacja ciasteczek z czekaniem na selektor
        try:
            page.wait_for_selector("button[data-role='accept-consent']", timeout=5000)
            page.click("button[data-role='accept-consent']")
        except:
            pass

        # Czekamy na pole wyszukiwania i używamy bardziej precyzyjnego selektora
        search_input = page.wait_for_selector("input[data-role='search-input']", timeout=10000)
        search_input.fill("laptop")

        page.keyboard.press("Enter")

        # Czekamy na wyniki wyszukiwania
        page.wait_for_selector("article[data-role='offer']", timeout=10000)

        # Zapisujemy zrzut ekranu
        page.screenshot(path="allegro_search.png")

        # Użycie bardziej niezawodnego selektora dla produktów
        products = page.query_selector_all("article[data-role='offer'] h2")[:5]

        for i, product in enumerate(products):
            print(f"{i + 1}. {product.inner_text()}")

        browser.close()


if __name__ == '__main__':
    allegro_search()
