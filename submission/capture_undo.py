import os
from playwright.sync_api import sync_playwright

abs_path = os.path.abspath('prototype/index.html')
file_url = 'file:///' + abs_path.replace('\\', '/')

with sync_playwright() as p:
    browser = p.chromium.launch(channel='msedge', headless=True)
    page = browser.new_page(viewport={'width': 1280, 'height': 900})
    page.goto(file_url)
    page.wait_for_timeout(1000)
    
    # Tap Majestic
    page.locator('.dest-card', has_text='Majestic').first.click()
    page.wait_for_timeout(300)
    page.locator('.pax-btn', has_text='3').first.click()
    page.wait_for_timeout(300)
    page.locator('#issueBtn').first.click()
    
    # Wait for success screen -> auto-return to destination screen with UNDO MODE active (after ~1.9s)
    page.wait_for_timeout(2200)
    phone = page.locator('.phone-frame')
    phone.screenshot(path='submission/screenshots/04_undo_active_grid.png')
    print('Captured 04_undo_active_grid.png successfully!')
    
    browser.close()
