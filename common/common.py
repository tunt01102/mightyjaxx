# browser_utils.py
from playwright.async_api import Page
import allure
class CommonActions:
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
        allure.attach(screenshot, name="Screenshot", attachment_type=allure.attachment_type.PNG)

