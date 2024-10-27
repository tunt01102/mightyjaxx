from config.import_all import *  # Import everything from import_all.py

# Test case home_001: Check about us page and blogs page


@pytest.mark.asyncio
@pytest.mark.regression
@allure.title("Test homepage 002: Goto About Us Page And Blogs Page")
async def testcase001_check_about_us_page():
    async with async_playwright() as playwright:

        # Call pre_step to handle setup tasks
        browser, context, page, date_folder, home_page, about_us_page, blogs_page = await pre_step(playwright)

        # Step 1: Go to Mighty Jaxx homepage
        await home_page.navigate_to_homepage()
        await page.wait_for_load_state('networkidle')
        expected_home_page_title = "Mighty Jaxx HQ - Designer Toys, Action Figures & Limited Edition Items"
        await CommonActions.check_title(page, expected_home_page_title)
        print("Step test 1: Go to home page and check home page title.")

        # Dismiss popups again in case they appear after navigating
        # await page.fill("//input[@type='email' and @placeholder='Enter your email address']", "your_email@example.com")
        # await page.click("//button[text()='Subscribe']")
        await page.keyboard.press("Escape")
        # await home_page.new_subscribe("tunt01102@gmail.com")
        # await page.mouse.dblclick(200, 200)
        await home_page.cookie_manager()

        # Step 2: Click on the 'About Us' link
        await page.locator("text=About Us").click()
        new_about_us_page = await context.wait_for_event("page")
        await new_about_us_page.wait_for_load_state("domcontentloaded")
        print("Step test 2.1: Click to 'About us'")

        # Step 3: Check page title
        expected_about_us_title = "The Mighty Jaxx Group"
        await CommonActions.check_title(new_about_us_page, expected_about_us_title)
        print("Step test 2.2: Check 'About us' page title")

        # Step 3 take a full screenshot of the 'About Us' page
        about_us_screenshot = await new_about_us_page.screenshot(path=f"evidences/{date_folder}/about_us.png", full_page=True)
        # Attach the screenshot to the Allure report
        allure.attach(about_us_screenshot, name="about_us_screenshot", attachment_type=allure.attachment_type.PNG)
        print("Step test 2.3: Take screenshot of About Us page.")

        # Step 5: Go back to the homepage
        await CommonActions.close_tab(new_about_us_page)
        print("Step test 2.4: Closed the About Us tab.")

        # Step 6: Click on the 'Blogs' link
        await page.locator("text=Blogs").click()
        await CommonActions.check_title(page, "Blogs")
        print("Step test 3.1: Open the blogs page.")

        # Step 7:Take a full screenshot of the 'Blogs' page
        await page.wait_for_load_state("networkidle")
        blogs_screenshot = await page.screenshot(path=f"evidences/{date_folder}/blogs_page.png", full_page=True)
        # Attach the screenshot to the Allure report
        allure.attach(blogs_screenshot, name="blogs_screenshot", attachment_type=allure.attachment_type.PNG)
        print("Step test 3.2: Take screen shot of Blogs page.")

        # Post step:  Close the browser
        await browser.close()
