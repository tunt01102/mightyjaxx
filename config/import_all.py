import asyncio
import allure
import subprocess
import pytest
import os
from playwright.async_api import async_playwright
from datetime import datetime

from config.environment import Config
from pages.home_page import HomePage
from pages.about_us_page import AboutUsPage
from pages.blogs_page import BlogsPage
from common.popup_utils import dismiss_popups
from common.common import CommonActions

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