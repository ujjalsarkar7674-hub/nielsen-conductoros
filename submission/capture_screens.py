import os
from playwright.sync_api import sync_playwright

abs_path = os.path.abspath('prototype/index.html')
file_url = 'file:///' + abs_path.replace('\\', '/')

os.makedirs('submission/screenshots', exist_ok=True)

with sync_playwright() as p:
    browser = p.chromium.launch(channel='msedge', headless=True)
    page = browser.new_page(viewport={'width': 1280, 'height': 900})
    page.goto(file_url)
    page.wait_for_timeout(1000)
    
    # 1. Main destination grid (phone frame only)
    phone = page.locator('.phone-frame')
    phone.screenshot(path='submission/screenshots/01_main_grid.png')
    print('Captured 01_main_grid.png')
    
    # 2. Tap Majestic to go to config screen
    page.locator('.dest-card', has_text='Majestic').first.click()
    page.wait_for_timeout(500)
    page.locator('.pax-btn', has_text='3').first.click()
    page.wait_for_timeout(500)
    phone.screenshot(path='submission/screenshots/02_ticket_config.png')
    print('Captured 02_ticket_config.png')
    
    # 3. Issue ticket -> Success screen
    page.locator('#issueTicketBtn, .issue-btn, button:has-text("Issue Ticket")').first.click()
    page.wait_for_timeout(600)
    phone.screenshot(path='submission/screenshots/03_ticket_success.png')
    print('Captured 03_ticket_success.png')
    
    # Reload and switch to sunlight mode
    page.goto(file_url)
    page.wait_for_timeout(500)
    sunlight_btn = page.locator('button:has-text("Sunlight")').first
    if sunlight_btn.count() > 0:
        sunlight_btn.click()
        page.wait_for_timeout(500)
        phone.screenshot(path='submission/screenshots/05_sunlight_mode.png')
        print('Captured 05_sunlight_mode.png')
        
    browser.close()
print('All screenshots captured successfully!')
