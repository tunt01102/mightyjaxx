async def dismiss_popups(page):
    # Dismiss the new user popup if it appears
    try:
        new_user_popup_visible = await page.locator("id = title-Close dialog").is_visible(timeout=2000)
        if new_user_popup_visible:
            new_user_email_selector = "id='email_119411823'"
            await page.fill(new_user_email_selector, "tunt01102@gmail.com")
            await page.click("class="needsclick go300628013 kl-private-reset-css-Xuajs1")
            #await page.click("id= title-Close dialog")
            print("New user popup dismissed.")
    except Exception as e:
        print("No new user popup to dismiss or error occurred:", str(e))

    # Dismiss the cookie consent if it appears
    try:
        cookie_consent_visible = await page.locator("text='Accept all'").is_visible(timeout=2000)
        if cookie_consent_visible:
            await page.click("text='Accept all'")
            print("Cookie consent dismissed.")
    except Exception as e:
        print("No cookie consent popup to dismiss or error occurred:", str(e))
