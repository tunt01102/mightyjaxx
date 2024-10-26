from mightyjaxx.import_all import *  # Import everything from import_all.py

#Test case 001: Check about us page and blogs page
async def testcase001_check_about_us_page():
    async with async_playwright() as playwright:
        # Call pre_step to handle setup tasks
        browser, context, page, date_folder, home_page, about_us_page, blogs_page = await pre_step(playwright)
        # Test Steps
        # Step 1: Go to Mighty Jaxx homepage
        await home_page.navigate_to_homepage()
        # Dismiss popups again in case they appear after navigating
        await dismiss_popups(page)
        # Step 2: Click on the 'About Us' link
        new_tab = await home_page.click_about_us()

        # Step 3 + 4: Scroll down to take a full screenshot of the 'About Us' page
        #await new_tab.evaluate("window.scrollTo(0, document.body.scrollHeight);")  # Scroll to the bottom
        await new_tab.screenshot(path=f"evidences/{date_folder}/about_us_page_full.png", full_page=True)
        print("Full screenshot of About Us page taken.")

        # Step 5: Go back to the homepage
        await new_tab.close()
        print("Closed the About Us tab.")

        # Dismiss popups again in case they appear after navigating
        await dismiss_popups(page)

        # Step 6: Click on the 'Blogs' link
        new_tab = await home_page.click_blogs()  # Assuming this also opens a new tab

        # Step 7: Scroll down to take a full screenshot of the 'Blogs' page
        await new_tab.evaluate("window.scrollTo(0, document.body.scrollHeight);")  # Scroll to the bottom
        await new_tab.screenshot(path=f"test_evidences/{date_folder}/blogs_page_full.png", full_page=True)
        print("Full screenshot of Blogs page taken.")
        # Step 8: Close the new tab
        await new_tab.close()
        print("Closed the Blogs tab.")

        # Post step:  Close the browser
        await browser.close()


