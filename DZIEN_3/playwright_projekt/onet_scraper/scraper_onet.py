from playwright.sync_api import sync_playwright

def scrape_onet_titles():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://www.onet.pl",timeout=60000)
        page.wait_for_selector("h2")
        titles = page.query_selector_all("h2")
        for i,title in enumerate(titles[:10]):
            print(f"{i+1}. {title.inner_text()}")
        browser.close()

if __name__ == '__main__':
    scrape_onet_titles()
