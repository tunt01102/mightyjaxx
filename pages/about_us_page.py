from playwright.async_api import Page

class AboutUsPage:
    def __init__(self, page: Page):
        self.page = page
        self.back_homepage_button = page.locator('//header/nav[1]/div[1]/a[1]')

    async def take_screenshot(self, path):
        await self.page.screenshot(path=path)

    async def click_back_to_homepage(self):
        await self.back_homepage_button.click()
        await self.page.wait_for_load_state("networkidle")
