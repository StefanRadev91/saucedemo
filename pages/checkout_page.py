from playwright.sync_api import Page 

class CheckoutPage:
    def __init__(self, page: Page):
        self.page = Page
        self.firstname = page.locator("#first-name")
        self.lastname = page.locator ("#last-name")
        self.postcode = page.locator ("#postal-code")
        self.buttoncontinue = page.locator ("#continue") 
        self.finishbutton = page.locator("#finish")

    def checkoutpage_flow(self, firstname: str, lastname: str, postcode: str):
        self.firstname.fill(firstname)
        self.lastname.fill(lastname)
        self.postcode.fill(postcode)
        self.buttoncontinue.click()
        self.finishbutton.click()

    def istheorderfinished(self):
        return self.page.locator("#checkout_complete_container > h2")
        
        