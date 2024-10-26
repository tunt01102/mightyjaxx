from playwright.async_api import Page

class BlogsPage:
    def __init__(self, page: Page):
        self.page = page

    async def take_screenshot(self, path):
        await self.page.screenshot(path=path)
