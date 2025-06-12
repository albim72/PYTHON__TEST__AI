from playwright.sync_api import sync_playwright

GITHUB_USER = "marcinal72"
GITHUB_PASSWORD = "nowarakieta2025"

def login_and_list_repos():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://github.com/login")
        page.wait_for_selector("input[name=login]")
        page.fill("input[name='login']", GITHUB_USER)
        page.fill("input[name='password']", GITHUB_PASSWORD)
        page.click("input[name=commit]")
        page.wait_for_url("https://github.com/*")

        page.goto(f"https://github.com/{GITHUB_USER}?tab=repositories")
        page.wait_for_selector("h3 a")
        repos = page.query_selector_all("h3 a")
        print("Repozytoria:")
        for repo in repos:
            print("- " + repo.inner_text())
        browser.close()

if __name__ == '__main__':
    login_and_list_repos()
