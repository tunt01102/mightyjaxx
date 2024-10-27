from config.import_all import *
import pytest
from playwright.async_api import async_playwright
from datetime import datetime
import os


class BrowserHelper:
    @staticmethod
    async def check_title(page, expected_title):
        actual_title = await page.title()
        assert actual_title == expected_title, f"Expected '{expected_title}', but got '{actual_title}'"

    @staticmethod
    async def close_tab(page):
        await page.close()

    @staticmethod
    async def scroll_and_screenshot(page, screenshot_path):
        # Scroll to the browser
        await page.evaluate("""
            const scrollToBottom = () => {
                return new Promise((resolve) => {
                    const distance = 100; 
                    const timer = setInterval(() => {
                        const scrollHeight = document.body.scrollHeight;
                        window.scrollBy(0, distance);
                        if ((window.innerHeight + window.scrollY) >= scrollHeight) {
                            clearInterval(timer);
                            resolve();
                        }
                    }, 100);
                });
            };
            scrollToBottom();
        """)

        # Take screenshot
        screenshot = await page.screenshot(path=screenshot_path, full_page=True)

        # Attach the screenshot to the Allure report
        allure.attach(screenshot, name=screenshot_path, attachment_type=allure.attachment_type.PNG)


@pytest.mark.asyncio
@allure.title("Test homepage 001: Goto About Us Page And Blogs Page (Scroll)")
@pytest.mark.regression
async def test_scenario_001():
    async with async_playwright() as playwright:
        # Pre steps
        browser = await playwright.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()

        # 1. Go to home page
        await page.goto("https://www.mightyjaxx.com")
        await page.wait_for_load_state('networkidle')
        print("Step test 1: Go to home page.")

        # skip pop-ups
        await page.keyboard.press("Escape")
        await page.locator("text='Accept all'").is_visible(timeout=2000)
        await page.click("text='Accept all'")

        # 2. Click on About us
        await page.locator("text=About Us").click()
        new_tab = await context.wait_for_event("page")
        await new_tab.wait_for_load_state("domcontentloaded")

        # 3. Check the About Us title
        await BrowserHelper.check_title(new_tab, "The Mighty Jaxx Group")
        print("Step test 2: Go to About Us page and check the title.")

        # 4. Scroll down and take screenshot
        date_folder = datetime.now().strftime("%Y%m%d_%H%M")
        os.makedirs(f"evidences/{date_folder}", exist_ok=True)
        screenshot_path = f"evidences/{date_folder}/scroll_about_us_page.png"
        await BrowserHelper.scroll_and_screenshot(new_tab, screenshot_path)
        print("Step test 3: Scroll down and take the screenshot.")

        # 5. Close About us tab => Go to home page
        await BrowserHelper.close_tab(new_tab)
        print("Step test 4: Close new tab.")

        # 6. From Home page => Click Blogs
        await page.locator("text=Blogs").click()
        await BrowserHelper.check_title(page, "Blogs")
        screenshot_path = f"evidences/{date_folder}/scroll_blogs_page.png"
        await BrowserHelper.scroll_and_screenshot(page, screenshot_path)
        print("Step test 5: Open Blogs page => Scroll down and take the screenshot.")

        await browser.close()
