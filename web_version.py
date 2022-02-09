from playwright.sync_api import sync_playwright
import re

def to_roman_numerals(num_to_convert):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto('https://www.romannumerals.org/converter')
        page.fill('id=intnum', str(num_to_convert))
        page.click("button:has-text(\"Convert to Roman\")")
        result = page.query_selector('id=result').text_content()
        browser.close()
        return re.search(r'\d+ = (\S+)', result).group(1)
