# config/environment.py

from playwright.async_api import Playwright

class Config:
    BROWSER = "chromium"  # Change to "chromium", "firefox", or "webkit"
    HEADLESS = False      # Set headless mode, True or False
    WIDTH   = 1920        # Set browser width
    HEIGHT  = 1080        # Set browser height

    @staticmethod
    async def launch_browser(playwright: Playwright):
        # Get the browser type in lowercase
        browser_type = Config.BROWSER.lower()

        # Launch the browser based on the specified type
        if browser_type == "chromium":
            browser = await playwright.chromium.launch(headless=Config.HEADLESS)
        elif browser_type == "firefox":
            browser = await playwright.firefox.launch(headless=Config.HEADLESS)
        elif browser_type == "webkit":
            browser = await playwright.webkit.launch(headless=Config.HEADLESS)
        else:
            raise ValueError(f"Unsupported browser type: {Config.BROWSER}")

        # Create a new context with the specified viewport size
        context = await browser.new_context(viewport={'width': Config.WIDTH, 'height': Config.HEIGHT})

        return browser, context
