import asyncio
import os
from playwright.async_api import async_playwright
from datetime import datetime

from mightyjaxx.config.environment import Config
from mightyjaxx.pages.home_page import HomePage
from mightyjaxx.pages.about_us_page import AboutUsPage
from mightyjaxx.pages.blogs_page import BlogsPage
from mightyjaxx.common.popup_utils import dismiss_popups

async def pre_step(playwright):
    # Get the current date and time in YYYYMMDD_HHMM format
    date_time_folder = datetime.now().strftime("%Y%m%d_%H%M")

    # Create the directory for today's evidences
    os.makedirs(f"evidences/{date_time_folder}", exist_ok=True)

    # Launch the browser and create a context with the configuration
    browser, context = await Config.launch_browser(playwright)
    page = await context.new_page()

    # Dismiss popups before starting tests
    await dismiss_popups(page)

    # Instantiate Page Objects
    home_page = HomePage(page)
    about_us_page = AboutUsPage(page)
    blogs_page = BlogsPage(page)

    return browser, context, page, date_time_folder, home_page, about_us_page, blogs_page