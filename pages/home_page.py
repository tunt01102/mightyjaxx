from playwright.async_api import Page
from playwright.async_api import async_playwright
class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.about_us_link = page.locator('//h2[contains(.,"About Us")]')
        self.new_user_popup_close_button = page.locator('title#title-Close dialog')
        self.cookie_popup_accept_button = page.locator('button:has-text("Accept all")')
        self.new_email_input = page.locator('//input[@id="email_119411823"]')
    async def handle_popups(self):
        # Handle the new user pop-up
        if await self.new_user_popup_close_button.is_visible():
            await self.new_user_popup_close_button.click()

        # Handle the cookie consent pop-up
        if await self.cookie_popup_accept_button.is_visible():
            await self.cookie_popup_accept_button.click()
    async def click_about_us(self):
        await self.about_us_link.click()
        #await self.page.goto("https://www.mightyjaxxgroup.com/")
        await self.page.wait_for_load_state("networkidle")

    async def click_blogs(self):
        await self.page.locator('//h2[contains(.,"Blogs")]').click()
        await self.page.wait_for_load_state("networkidle")
    async def navigate_to_homepage(self):
        await self.page.goto("https://www.mightyjaxx.com")
        await self.handle_popups()  # Check and handle popups after page loads

    async def new_subscribe(self, email):
        await self.new_email_input.is_visible()
        await self.page.fill("//input[@type='email' and @placeholder='Enter your email address']", email)
        await self.page.click("//button[text()='Subscribe']")
        await self.page.keyboard.press("Escape")
        print(f"new subscribe done")

    async def close_all_popups(self):
        close_buttons_selectors = [
            'button.close',
            'button[data-dismiss="modal"]',
            'circle[style*="cursor: pointer;"]',
            'div.close',

        ]
        for selector in close_buttons_selectors:
            try:
                await self.page.wait_for_selector(selector, timeout=2000)
                await self.page.click(selector)
                print(f"Closed the pop-up by selector: {selector}")
            except Exception as e:
                print(f"pop-up not found with selector: {selector}. Error: {str(e)}")

    async def cookie_manager(self):
        # Dismiss the cookie consent if it appears
        try:
            cookie_consent_visible = await self.page.locator("text='Accept all'").is_visible(timeout=2000)
            if cookie_consent_visible:
                await self.page.click("text='Accept all'")
                print("Cookie consent dismissed.")
        except Exception as e:
            print("No cookie consent popup to dismiss or error occurred:", str(e))