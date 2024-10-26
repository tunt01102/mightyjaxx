from playwright.async_api import Page
class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.about_us_link = page.locator('//h2[contains(.,"About Us")]')
        self.new_user_popup_close_button = page.locator('#title-Close\\ dialog')
        self.cookie_popup_accept_button = page.locator('button:has-text("Accept all")')
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